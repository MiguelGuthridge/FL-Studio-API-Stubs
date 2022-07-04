"""
channels > properties

Function definitions for managing channel properties.
"""
import midi
from .__helpers import checkGroupIndex


def channelNumber(canBeNone: bool = False, offset: int = 0) -> int:
    """Returns the global index of the first selected channel, otherwise the
    nth selected channel where n is `offset` + 1. If n is greater than the
    number of selected channels, the global index of the last selected channel
    will be returned.

    If `canBeNone` is `1`, no selection will return `-1`. Otherwise, no
    selection will return `0` (representing the first channel).

    ## Args:
    * `canBeNone` (`bool`, optional): Whether the function will return `-1` or
      `0` when there is no selection. Defaults to `False` (returning `0`).

    * `offset` (`int`, optional): return other selected channels after offset.
      Defaults to 0.

    ## Returns:
    * `int`: global index of first selected channel

    Included since API version 1
    """
    return 0


def channelCount(mode: bool = False) -> int:
    """Returns the number of channels on the channel rack. Respect for groups
    is controlled by the `mode` flag.

    ## Args:
    * `mode` (`bool`, optional): Whether the number of channels should be
      global. Defaults to `False` (groups respected).

    ## Returns:
    * `int`: number of channels

    Included since API version 1. (updated with optional parameter in API
    version 3).
    """
    return 0


def getChannelName(index: int) -> str:
    """Returns the name of the channel at `index` (respecting groups)

    ## Args:
     * `index` (`int`): index of channel

    ## Returns:
     * `str`: channel name

    Included since API version 1
    """
    checkGroupIndex(index)
    return ""


def setChannelName(index: int, name: str) -> None:
    """Sets the name of the channel at `index` (respecting groups)

    If a channel's name is set to "", its name will be set to the default name
    of the plugin or sample.

    ## Args:
     * `index` (`int`): index of channel

     * `name` (`str`): new name for channel

    Included since API version 1
    """
    checkGroupIndex(index)


def getChannelColor(index: int) -> int:
    """Returns the color of the channel at `index` (respecting groups)

    Note that colors can be split into or built from components using the
    functions provided in the module `utils`

    * `ColorToRGB()`

    * `RGBToColor()`

    ## Args:
     * `index` (`int`): index of channel

    ## Returns:
     * `int`: channel color (0x--BBGGRR)

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0


def setChannelColor(index: int, color: int) -> None:
    """Sets the color of the channel at `index` (respecting groups)

    Note that colors can be split into or built from components using the
    functions provided in the module `utils`

    * `ColorToRGB()`

    * `RGBToColor()`

    ## Args:
     * `index` (`int`): index of channel
     * `color` (`int`): new color for channel (0x--BBGGRR)

    Included since API version 1
    """
    checkGroupIndex(index)


def isChannelMuted(index: int) -> bool:
    """Returns whether channel is muted (`1`) or not (`0`)

    ## Args:
     * `index` (`int`): index of channel

    ## Returns:
     * `bool`: mute status

    Included since API version 1
    """
    checkGroupIndex(index)
    return False


def muteChannel(index: int) -> None:
    """Toggles the mute state of the channel at `index`

    ## Args:
     * `index` (`int`): index of channel
    """
    checkGroupIndex(index)


def isChannelSolo(index: int) -> bool:
    """Returns whether channel is solo (`1`) or not (`0`)

    ## Args:
     * `index` (`int`): index of channel

    ## Returns:
     * `bool`: solo status

    Included since API version 1
    """
    checkGroupIndex(index)
    return False


def soloChannel(index: int) -> None:
    """Toggles the solo state of the channel at `index`

    ## Args:
     * `index` (`int`): index of channel

    Included since API version 1
    """
    checkGroupIndex(index)


def getChannelVolume(index: int, mode: bool = False) -> float:
    """Returns the normalized volume of the channel at `index`, where `0.0` is
    the minimum value, and `1.0` is the maximum value. Note that the default
    volume for channels is `0.78125`. By setting the `mode` flag to `True`, the
    volume is returned in decibels.

    ## Args:
    * `index` (`int`): index of channel

    * `mode` (`int`, optional): whether to return as a float between 0 and 1
      (`False`) or a value in dB (`True`)

    ## Returns:
    * `float`: channel volume

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0.0


def setChannelVolume(
    index: int,
    volume: float,
    pickupMode: int = midi.PIM_None
) -> None:
    """Sets the normalized volume of the channel at `index`, where `0.0` is
    the minimum value, and `1.0` is the maximum value. Note that the default
    volume for channels is `0.78125`. Use the pickup mode flag to set pickup
    options.

    ## Args:
     * `index` (`int`): index of channel

     * `volume` (`float`): channel volume

     * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
       the [manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#pickupModes)

    Included since API version 1
    """
    checkGroupIndex(index)


def getChannelPan(index: int) -> float:
    """Returns the normalized pan of the channel at `index`, where `-1.0` is
    100% left, and `1.0` is 100% right. Note that the default pan for channels
    is `0.0` (centre).

    ## Args:
     * `index` (`int`): index of channel

    ## Returns:
     * `float`: channel pan

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0.0


def setChannelPan(index: int, pan: float, pickupMode: int = midi.PIM_None) -> None:
    """Sets the normalized pan of the channel at `index`, where `-1.0` is
    100% left, and `1.0` is 100% right. Note that the default
    pan for channels is `0.0` (centre). Use the pickup mode flag to set pickup
    options.

    ## Args:
     * `index` (`int`): index of channel

     * `pan` (`float`): channel pan

     * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
       the [manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#pickupModes)

    Included since API version 1
    """
    checkGroupIndex(index)


def getChannelPitch(index: int, mode: int = 0) -> 'float | int':
    """Returns the current pitch bend (or range) of the channel at `index`.
    The `mode` parameter is used to determine the type of pitch returned.

    ## Args:
    * `index` (`int`): index of channel

    * `mode` (`int`, optional):
          * `0` (default): return the current pitch bend as a factor of the current
              range (usually `-1.0` to `1.0`). Larger values might be reached if the
              pitch is automated with events, for example.

          * `1`: return the current pitch offset in cents.
              * BUG: Official API docs incorrectly state "semitones".

          * `2`: return the current pitch range in semitones.
              * BUG: This is not guaranteed to be correct.
                For more information, see `setChannelPitch` on
                modifying the pitch range of a channel.

    ## Returns:
     * `float`: channel pitch (when `mode` is `0`)

     * `int`: channel pitch range (when `mode` is `1` or 2)

    Included since API version 8
    """
    checkGroupIndex(index)
    return 0


def setChannelPitch(index: int, value: float, mode: int = 0, pickupMode: int = midi.PIM_None) -> 'float | int':
    """Sets the pitch of the channel at `index` to value. The `mode` parameter is used
    to determine the type of pitch set. Use the pickup mode flag to set pickup
    options. The final pitch will be clamped to the current pitch range.

    ## Args:
     * `index` (`int`): index of channel

     * `value` (`float`): value to set

     * `mode` (`int`, optional):
          * `0` (default): set pitch as a factor of the current pitch bend range (between [-1.0, 1.0]).

          * `1`: set pitch in cents

          * `2`: **UTTERLY BROKEN.** Set the pitch range in semitones.

            BUG: This only affects the range reported by `getChannelPitch`.
            This will desynchronize the reported range from what is visible in the UI.

     * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
       the [manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#pickupModes)

    Included since API version 8
    """
    checkGroupIndex(index)
    return 0


def getChannelType(index: int) -> int:
    """
    Returns the type of instrument loaded into the channel rack at `index`

    ## Args:
    * `index` (`int`): index of channel


    ## Returns:
    * `int`: type of channel:
          * `GT_Sampler` (`0`): internal sampler

          * `GT_Hybrid` (`1`): generator plugin feeding internal sampler

          * `GT_GenPlug` (`2`): generator plugin

          * `GT_Layer` (`3`): layer (refer to the [FL Studio Manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_layer.htm))

          * `GT_AutoClip` (`4`): automation clip

    Included since API Version 19
    """
    checkGroupIndex(index)
    return 0


def isChannelSelected(index: int) -> bool:
    """Returns whether the channel at `index` is selected (not respecting
    channel groups).

    ## Args:
     * `index` (`int`): channel index

    ## Returns:
     * `bool`: whether the channel is selected

    Included since API version 1
    """
    checkGroupIndex(index)
    return False


def selectChannel(index: int, value: int = -1) -> None:
    """Select the channel at `index` (respecting groups).

    ## Args:
     * `index` (`int`): channel index

     * `value` (`int`, optional): Whether to select or deselect the channel.
          * `-1` (default): Toggle

          * `0` : Deselect

          * `1`: Select

    Included since API version 1
    """
    checkGroupIndex(index)


def selectOneChannel(index: int) -> None:
    """Exclusively select the channel at `index` (deselecting any other selected
    channels).

    ## Args:
     * `index` (`int`): channel index

    Included since API version 8
    """
    checkGroupIndex(index)


def selectedChannel(canBeNone: int = 0, offset: int = 0, indexGlobal: int = 0) -> int:
    """Returns the index of the first selected channel, otherwise the nth
    selected channel where n is `offset` + 1. If n is greater than the number of
    selected channels, the global index of the last selected channel will be
    returned. If `indexGlobal` is set to `1`, this will replicate the behavior
    of `channelNumber()` by returning global indexes.

    ## NOTE:
    * This function replaces the functionality of `channelNumber()`
      entirely, with the added functionality of providing indexes respecting
      groups (when `indexGlobal` is not set).

    If `canBeNone` is `1`, no selection will return `-1`. Otherwise, no selection
    will return `0` (representing the first channel).

    ## Args:
     * `canBeNone` (`int`, optional): Whether the function will return `-1` or
       `0` when there is no selection. Defaults to `0` (returning `0`).

     * `offset` (`int`, optional): return other selected channels after offset.
       Defaults to 0.

     * `indexGlobal` (`int`, optional): Whether to return the group index (`0`)
       or the global index (`1`).

    ## Returns:
     * `int`: index of first selected channel

    Included since API version 5
    """
    return 0


def selectAll() -> None:
    """Selects all channels in the current channel group

    Included since API version 1
    """


def deselectAll() -> None:
    """Deselects all channels in the current channel group

    Included since API version 1
    """


def getChannelMidiInPort(index: int) -> int:
    """Returns the MIDI port associated with the channel at `index`.

    This can be used to send data directly to channels that are associated with
    a MIDI in port. Although channels are unassigned by default, a user can
    configure plugins to receive MIDI on a certain channel which can unlock
    many useful plugin-specific features.

    ## Args:
     * `index` (`int`): channel index

    ## Returns:
     * `int`: MIDI port associated with channel

     * `-2`: Channel not assigned to a MIDI port

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0


def getChannelIndex(index: int) -> int:
    """Returns the global index of a channel given the group `index`.

    ## Args:
     * `index` (`int`): index of channel (respecting groups)

    ## Returns:
     * `int`: global index of channel

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0


def getTargetFxTrack(index: int) -> int:
    """Returns the mixer track that the channel at `index` is linked to.

    ## Args:
     * `index` (`int`): index of channel

    ## Returns:
     * `int`: index of targeted mixer track

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0


def processRECEvent(eventId: int, value: int, flags: int) -> int:
    """Processes a recording event.

    ## WARNING:
    * This function is depreciated here, and moved to the `general` module as
      of API version 7.

    ## Args:
     * `eventId` (`int`): Refer to the [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#RecEventParams)

     * `value` (`int`): value of even within range (0 - midi.FromMIDI_Max)

     * `flags` (`int`): Refer to the [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#RecEventFlags)

    ## Returns:
     * `int`: Unknown

    Included since API version 1
    Depreciated since API version 7
    """
    return 0


def incEventValue(eventId: int, step: int, res: float = 1 / 24) -> int:
    """Get event value increased by step. Use (optional) res parameter to
    specify increment resolution.

    Use result as new value in processRECEvent

    ## Example usage:
    ```py
    # Increase volume of first channel
    step = 1
    eventId = midi.REC_Chan_Vol + channels.getRecEventId(0)
    newValue = channels.incEventValue(eventId, step)
    general.processRECEvent(eventId, newValue, midi.REC_UpdateValue | midi.REC_UpdateControl)
    ```

    ## Args:
     * `eventId` (`int`): event ID, see the [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#RecEventParams)

     * `step` (`int`): event value increased by step

     * `res` (`float`, optional): increment resolution. Defaults to 1/24.

    ## Returns:
     * `int`: incremented event value, for use in `general.processRECEvent()`

    Included since API version 1
    """
    return 0


def getRecEventId(index: int) -> int:
    """Return the starting point of REC event IDs for the channel at `index`.

    See `general.processRECEvent` for more information.

    ## Args:
     * `index` (`int`): channel index

    ## Returns:
     * `int`: REC event ID offset for accessing `midi.REC_Chan_*` parameters

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0
