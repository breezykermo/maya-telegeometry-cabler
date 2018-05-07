# Maya TeleGeometry Cabler

Aa library for projecting [data regarding underseas cables](https://www.submarinecablemap.com/) to a stylized representation in [Maya](https://www.autodesk.com/products/maya/overview).

![cabled globe screenshot](/cabled-globe.jpeg)

You will need Maya installed and open, as the script needs to be run through Maya's Python engine. You will also need to install the libraries listed in [requirements.txt](/requirements.txt) on your system so that they are available to the Maya runtime. See [this document](http://help.autodesk.com/view/MAYAUL/2018/ENU/?guid=__files_GUID_130A3F57_2A5D_4E56_B066_6B86F68EEA22_htm) for information on where you can find this on your system. You will also need to make [Cabler.py](/lib/Cabler.py) available to the Maya runtime in the same way.

Once this is done, you can either copy and paste the script direct into Maya's Script Editor, or use [this Sublime Text plugin](https://github.com/justinfx/MayaSublime) to send code from Sublime to Maya via commandPort. See [examples.py](/examples.py) for a brief overview of the functions available.

As explained in the source code comments, the data from TeleGeometry's [Submarine Cable Map](https://www.submarinecablemap.com/) is inlined, to minimize import difficulties. It was distilled from [its actively developed source](https://github.com/telegeography/www.submarinecablemap.com) in February 2018, and may therefore be slightly out of date. 