# Rating-Converter
## What Does It Do?
- Rating Converter is used to covert ratings between different scales.
- Rating Scales is used to list details about the different ranges.

# Reason For Creation
Made this to convert between different rating systems. I prefer using a more linear scale for quality, but it seems like everyone is still stuck using a school grading scale.

# Running The Python Scripts
### Windows
- Initial Run
    - cd /your/folder
    - python3 -m venv env
    - call env/Scripts/activate.bat
    - python3 -m pip install -r requirements.txt
    - Depending on which script
        - python3 Rating_Converter.py
        - python3 Rating_Scales.py
- Running After
    - cd /your/folder
    - Depending on which script
        - call env/Scripts/activate.bat && python3 Rating_Converter.py
        - call env/Scripts/activate.bat && python3 Rating_Scales.py
- Running Without Terminal Staying Around
    - Change the file type from py to pyw
    - You should just be able to click the file to launch it
    - May need to also change python3 to just python if it doesn't work after the change
        - In the first line of the code change python3 to python
### Linux
- Initial Run
    - cd /your/folder
    - python3 -m venv env
    - source env/bin/activate
    - python3 -m pip install -r requirements.txt
    - Depending on which script
        - python3 Rating_Converter.py
        - python3 Rating_Scales.py
- Running After
    - cd /your/folder
    - Depending on which script
        - source env/bin/activate && python3 Rating_Converter.py
        - source env/bin/activate && python3 Rating_Scales.py
- Running Without Terminal Staying Around
    - Run the file with nohup
    - May have to set executable if it's not already
        - chmod +x Pomodoro_Alerts.py
