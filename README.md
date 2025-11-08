# Waste-Less

## Setup

### 1. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Set up Gemini API Key

**Recommended: Using a .env file (easiest method)**

1. Create a `.env` file in the project root directory
2. Add your API key to the file:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```
3. Replace `your-api-key-here` with your actual Gemini API key

**Note:** The `.env` file is automatically loaded by the script. Make sure not to commit this file to git (it should be in `.gitignore`).

**Alternative: Using environment variables directly**

If you prefer not to use a `.env` file, you can set the environment variable directly:

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**On Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**On Linux/Mac:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Get your API key:** You can get one from [Google AI Studio](https://makersuite.google.com/app/apikey).

### 3. Run the Script

**On Windows (Recommended):**
```powershell
py AI_stuff\setup.py
```

**On Linux/Mac:**
```bash
python AI_stuff/setup.py
```

**Note:** On Windows, if you have multiple Python installations, use `py` instead of `python` to ensure you're using the correct Python version that has the packages installed.
