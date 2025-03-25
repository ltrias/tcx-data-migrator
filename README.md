# TCX Data Migrator 
Allows to merge data from a TCX file into another one.

### Example usage scenario

You used a H10 heart rate monitor from Polar to record your heart rate during a swimming session and your Garmin watch to monitor everything else. Polar strap won't download recorded data to Garmin watch, so you will have precise heart data on polar flow and other swimming metrics on Garmin connect

You can export both activities TCX files using [Garmin Connect](https://connect.garmin.com/) and [Polar Flow](https://flow.polar.com/) and merge the preciase heart rate data into the metrics from garmin watch

As it's very hard to match different devices reading down to millisecond precision, best effort will be used to approximate readings.

### Requirements
[Python](https://www.python.org/downloads/)