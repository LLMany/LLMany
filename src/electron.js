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
            preload: join(__dirname, 'preload'),
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

    // Handle Python process output
    pythonProcess.stdout.on('data', (data) => {
        const message = data.toString().trim();
        try {
            // Parse Python output as JSON
            const jsonData = JSON.parse(message);
            mainWindow.webContents.send('from-python', jsonData);
        } catch (e) {
            console.log('Python output:', message);
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

// Handle IPC messages from React
ipcMain.handle('to-python', async (event, data) => {
    if (pythonProcess && !pythonProcess.killed) {
        // Send data to Python process
        pythonProcess.stdin.write(JSON.stringify(data) + '\n');
        return { success: true };
    }
    return { success: false, error: 'Python process not running' };
});

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (pythonProcess) {
        pythonProcess.kill();
    }
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
