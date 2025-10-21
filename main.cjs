// main.cjs
const { Worker } = require('worker_threads');
const path = require('path');

console.log('Main thread: Starting...');

// Get absolute path of worker file
const workerPath = path.resolve(__dirname, 'worker.cjs');

// Create a worker
const worker = new Worker(workerPath, { workerData: 1000000 });

// Listen for messages
worker.on('message', (result) => {
  console.log('Result from worker:', result);
});

// Listen for errors
worker.on('error', (err) => {
  console.error('Worker error:', err);
});

// Listen for exit
worker.on('exit', (code) => {
  console.log(`Worker stopped with exit code ${code}`);
});
