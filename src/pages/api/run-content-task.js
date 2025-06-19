export const prerender = false;

import { json } from 'astro/runtime/server';

export async function post({ request }) {
  const { action } = await request.json();
  let message = '';
  try {
    // Windows için python komutu
    let pyCmd = 'python';
    if (process.platform === 'win32') pyCmd = 'python';
    let script = 'auto_content_generator.py';
    let args = [];
    if (action === 'daily') args = ['1'];
    else if (action === 'weekly') args = ['2'];
    else if (action === 'single') args = ['1'];
    else if (action === 'test') args = ['1'];
    else if (action === 'schedule') args = ['3'];

    const { spawn } = await import('child_process');
    return new Promise((resolve) => {
      const proc = spawn(pyCmd, [script, ...args], { cwd: process.cwd() });
      let output = '';
      proc.stdout.on('data', (data) => { output += data.toString(); });
      proc.stderr.on('data', (data) => { output += data.toString(); });
      proc.on('close', (code) => {
        message = output || (code === 0 ? 'İşlem tamamlandı.' : 'Bir hata oluştu.');
        resolve(json({ message }));
      });
    });
  } catch (err) {
    return json({ message: 'Sunucu hatası: ' + err.message });
  }
}
