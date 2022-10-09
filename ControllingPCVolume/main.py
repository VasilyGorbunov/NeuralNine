from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.SetMasterVolumeLevel(-20.0, None)
# volume.SetMute(1, None)

# current = volume.GetMasterVolumeLevel()
# volume.SetMasterVolumeLevel(current + 6.0, None)

sessions = AudioUtilities.GetAllSessions()
print()