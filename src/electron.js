const {app, BrowserWindow, ipcMain} = require('electron');
const {sep, resolve, join} = require("node:path");
const {spawn} = require("child_process");

let mainWindow;
let pythonProcess;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            preload: join(__dirname, 'preload.js'),
        },
    });

    const startURL = 'http://localhost:3000';

    mainWindow.loadURL(startURL);

    mainWindow.on('closed', () => (mainWindow = null));

    startPythonBackend();
}


app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    }
});

function startPythonBackend() {
    const dir = resolve(__dirname, '..');
    const scriptPath = join(dir, 'backend', 'llmany_backend', 'main.py');

    process.chdir('backend');
    pythonProcess = spawn('poetry', ['run', 'python', scriptPath]);
    process.chdir('..')
    console.log("Started backend")
    // Handle Python process output
    // pythonProcess.stdout.on('data', (data) => {
    //     const message = data.toString().split('\n')[0].trim();
    //     try {
    //         console.log('Received python data:\n' + message);
    //         // Parse Python output as JSON
    //         const jsonData = JSON.parse(message);
    //         if (mainWindow && !mainWindow.isDestroyed()) {
    //             console.log('Send to main process: ' + jsonData);
    //             mainWindow.webContents.send('from-python', jsonData);
    //         } else {
    //             console.log('mainWindow is not available.');
    //         }
    //     } catch (e) {
    //         console.log('Python output with exception:\n' + e + "\n" + message);
    //     }
    // });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

ipcMain.handle('to-python', async (event, data) => {
    console.log("Received request from rendered")
    console.log(JSON.stringify(data));
    if (pythonProcess && !pythonProcess.killed) {
        pythonProcess.stdin.write(JSON.stringify(data) + '\n');
    }
    return new Promise(async (resolve, reject) => {
        let message
        pythonProcess.stdout.on('data', (data) => {
            message = data.toString().split('\n')[0].trim();
            console.log("Message:\n" + message);
            resolve(message)
        })
        pythonProcess.on('close', (code) => {
            resolve(message)
        })
    })
})

const readResponse = async () => {
    return 1
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (pythonProcess) {
        pythonProcess.kill();
    }
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

ipcMain.handle('fetch-data', async (event, data) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(1)
        }, 1000)
    })
})