const {app, BrowserWindow, ipcMain} = require('electron');
const {sep, resolve, join, dirname} = require("node:path");
const {spawn} = require("child_process");

let mainWindow;
let pythonProcess;

function createWindow() {
    console.log(join(__dirname, 'public', 'preload.js'))
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: join(__dirname, 'public','preload.js'),
        },
    });

    const startURL = 'http://localhost:3000';

    mainWindow.loadURL(startURL);

    mainWindow.on('closed', () => (mainWindow = null));

    startPythonBackend();
}


function sendToAllWindows(channel, data) {
    BrowserWindow.getAllWindows().forEach(window => {
        if (!window.isDestroyed()) {
            window.webContents.send(channel, data);
        }
    });
}

app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    }
});

function startPythonBackend() {
    const scriptPath = join(__dirname, 'backend', 'llmany_backend', 'main.py');

    process.chdir('backend');
    pythonProcess = spawn('poetry', ['run', 'python', scriptPath]);
    process.chdir('..')
    console.log("Started backend")
    // Handle Python process output
    pythonProcess.stdout.on('data', (data) => {
        console.log("----\n" + data + "----\n");

        const message = data.toString().split('\n')[0].trim();

        console.log("Received python data in electron:\n" + message)
        try {
            // Parse Python output as JSON
            const jsonData = JSON.parse(message);
            if (mainWindow && !mainWindow.isDestroyed()) {
                console.log('Send to main process: ' + message);
                sendToAllWindows('from-python', message);
            } else {
                console.log('mainWindow is not available.');
                ipcMain.handle('from-python', jsonData);
            }
        } catch (e) {
            console.log('Python output with exception:\n' + e + "\n" + message);
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

ipcMain.on('to-python', (event, data) => {
    console.log("Received request from renderer")
    console.log(JSON.stringify(data));
    if (pythonProcess && !pythonProcess.killed) {
        pythonProcess.stdin.write(JSON.stringify(data) + '\n');
    }
})


app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (pythonProcess) {
        pythonProcess.kill();
    }
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
