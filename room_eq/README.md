Room Equalization Setup:

To setup each channel run this(not the regular "jalv -g" as it won't show the GUI correctly):


jalv.gtk3 http://lsp-plug.in/plugins/lv2/para_equalizer_x32_mono

Right click on the LSP PE32M -> Import -> Import REW, then Export -> Export Settings into File, select a new folder, as it saves into a folder instead of a file. 

Repeat for each channel.

Setting up JACK:
using KxStudio Cadence along with Claudia, jalv, and LSP-Plugins.


Didn't have to compile any of that, simple Ubuntu Apt install

Notes:

By setting up the Cadence to auto load a Ladish project, the JACK settings in Cadence are not used, and instead JACK is configured over D-Bus from settings in the Claudia/Ladish project(the Para LR.xml in .ladish/studios).

Put the .ladish folder into /home.

Cadence setup to forward ALSA -> Pulse -> JACK

REW notes:

JACK is configured to not touch the microphone as REW really wants it to either be sitting on ALSA or the Pulse, or else the calibration sensitivity reports wrong values all over the place.

Unlike Equalizer APO, export of EQ settings is with "Export filter settings as text", or else the Jalv can't load them.

Don't use Cadence PulseAudio Auto-Start at login feature as it loads some random script that doesn't work for me.

Disable "PulseAudio Sound System" in XFCE Sessions and Startup.

Keep "Cadence session startup" in XFCE Sessionsa nd Startup.

Looks like currently PulseAudio is started with "systemctl --user enable pulseaudio.socket/.service"

Don't bother messing with .config/jack.conf as it get overriden and never read from when started by Cadence.
