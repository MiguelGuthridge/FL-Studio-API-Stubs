
LATEST_API_VERSION = 23

# infinity
oo = float('inf')

DEFAULT_FL_COLOR = 0x5C656A

PATTERN_COUNT = 1000

DEFAULT_CHANNEL_VOLUME = 0.78125

VST_PARAM_COUNT = 4240

# Generate using
# for i in range(4096,4240): print(f'    {i}: "{plugins.getParamName(i, 0)}",')
VST_FINAL_PARAM_NAMES = {
    4096: "MIDI CC #0 (Bank select MSB)",
    4097: "MIDI CC #1 (Modulation wheel)",
    4098: "MIDI CC #2 (Breath controller)",
    4099: "MIDI CC #3",
    4100: "MIDI CC #4 (Foot controller)",
    4101: "MIDI CC #5 (Portamento time)",
    4102: "MIDI CC #6 (Data entry MSB)",
    4103: "MIDI CC #7 (Main volume)",
    4104: "MIDI CC #8 (Balance)",
    4105: "MIDI CC #9",
    4106: "MIDI CC #10 (Pan)",
    4107: "MIDI CC #11 (Expression controller)",
    4108: "MIDI CC #12 (Control 1)",
    4109: "MIDI CC #13 (Control 2)",
    4110: "MIDI CC #14",
    4111: "MIDI CC #15",
    4112: "MIDI CC #16 (General purpose controller 1)",
    4113: "MIDI CC #17 (General purpose controller 2)",
    4114: "MIDI CC #18 (General purpose controller 3)",
    4115: "MIDI CC #19 (General purpose controller 4)",
    4116: "MIDI CC #20",
    4117: "MIDI CC #21",
    4118: "MIDI CC #22",
    4119: "MIDI CC #23",
    4120: "MIDI CC #24",
    4121: "MIDI CC #25",
    4122: "MIDI CC #26",
    4123: "MIDI CC #27",
    4124: "MIDI CC #28",
    4125: "MIDI CC #29",
    4126: "MIDI CC #30",
    4127: "MIDI CC #31",
    4128: "MIDI CC #32 (Bank select LSB)",
    4129: "MIDI CC #33 (Modulation wheel LSB)",
    4130: "MIDI CC #34 (Breath controller LSB)",
    4131: "MIDI CC #35",
    4132: "MIDI CC #36 (Foot controller LSB)",
    4133: "MIDI CC #37 (Portamento time LSB)",
    4134: "MIDI CC #38 (Data entry LSB )",
    4135: "MIDI CC #39 (Main volume LSB)",
    4136: "MIDI CC #40 (Balance LSB)",
    4137: "MIDI CC #41",
    4138: "MIDI CC #42 (Pan LSB)",
    4139: "MIDI CC #43 (Expression controller LSB)",
    4140: "MIDI CC #44 (Control 1 LSB)",
    4141: "MIDI CC #45 (Control 2 LSB)",
    4142: "MIDI CC #46",
    4143: "MIDI CC #47",
    4144: "MIDI CC #48 (General purpose controller 1 LSB)",
    4145: "MIDI CC #49 (General purpose controller 2 LSB)",
    4146: "MIDI CC #50 (General purpose controller 3 LSB)",
    4147: "MIDI CC #51 (General purpose controller 4 LSB)",
    4148: "MIDI CC #52",
    4149: "MIDI CC #53",
    4150: "MIDI CC #54",
    4151: "MIDI CC #55",
    4152: "MIDI CC #56",
    4153: "MIDI CC #57",
    4154: "MIDI CC #58",
    4155: "MIDI CC #59",
    4156: "MIDI CC #60",
    4157: "MIDI CC #61",
    4158: "MIDI CC #62",
    4159: "MIDI CC #63",
    4160: "MIDI CC #64 (Damper pedal (sustain))",
    4161: "MIDI CC #65 (Portamento)",
    4162: "MIDI CC #66 (Sostenuto)",
    4163: "MIDI CC #67 (Soft pedal)",
    4164: "MIDI CC #68 (Legato footswitch)",
    4165: "MIDI CC #69 (Hold 2)",
    4166: "MIDI CC #70 (Sound variation)",
    4167: "MIDI CC #71 (Harmonic content)",
    4168: "MIDI CC #72 (Release time)",
    4169: "MIDI CC #73 (Attack time)",
    4170: "MIDI CC #74 (Brightness)",
    4171: "MIDI CC #75 (Sound controller 6)",
    4172: "MIDI CC #76 (Sound controller 7)",
    4173: "MIDI CC #77 (Sound controller 8)",
    4174: "MIDI CC #78 (Sound controller 9)",
    4175: "MIDI CC #79 (Sound controller 10)",
    4176: "MIDI CC #80 (General purpose controller 5)",
    4177: "MIDI CC #81 (General purpose controller 6)",
    4178: "MIDI CC #82 (General purpose controller 7)",
    4179: "MIDI CC #83 (General purpose controller 8)",
    4180: "MIDI CC #84 (Portamento control)",
    4181: "MIDI CC #85",
    4182: "MIDI CC #86",
    4183: "MIDI CC #87",
    4184: "MIDI CC #88",
    4185: "MIDI CC #89",
    4186: "MIDI CC #90",
    4187: "MIDI CC #91 (Reverb depth)",
    4188: "MIDI CC #92 (Tremolo depth)",
    4189: "MIDI CC #93 (Chorus depth)",
    4190: "MIDI CC #94 (Celeste depth)",
    4191: "MIDI CC #95 (Phaser depth)",
    4192: "MIDI CC #96 (Data increment)",
    4193: "MIDI CC #97 (Data decrement)",
    4194: "MIDI CC #98 (NRPN LSB)",
    4195: "MIDI CC #99 (NRPN MSB)",
    4196: "MIDI CC #100 (RPN LSB)",
    4197: "MIDI CC #101 (RPN MSB)",
    4198: "MIDI CC #102",
    4199: "MIDI CC #103",
    4200: "MIDI CC #104",
    4201: "MIDI CC #105",
    4202: "MIDI CC #106",
    4203: "MIDI CC #107",
    4204: "MIDI CC #108",
    4205: "MIDI CC #109",
    4206: "MIDI CC #110",
    4207: "MIDI CC #111",
    4208: "MIDI CC #112",
    4209: "MIDI CC #113",
    4210: "MIDI CC #114",
    4211: "MIDI CC #115",
    4212: "MIDI CC #116",
    4213: "MIDI CC #117",
    4214: "MIDI CC #118",
    4215: "MIDI CC #119",
    4216: "MIDI CC #120 (All sound off)",
    4217: "MIDI CC #121 (Reset all controllers)",
    4218: "MIDI CC #122 (Local control on/off)",
    4219: "MIDI CC #123 (All notes off)",
    4220: "MIDI CC #124 (Omni mode off)",
    4221: "MIDI CC #125 (Omni mode on)",
    4222: "MIDI CC #126 (Mono mode on)",
    4223: "MIDI CC #127 (Poly mode on)",
    4224: "MIDI Channel 1 Aftertouch",
    4225: "MIDI Channel 2 Aftertouch",
    4226: "MIDI Channel 3 Aftertouch",
    4227: "MIDI Channel 4 Aftertouch",
    4228: "MIDI Channel 5 Aftertouch",
    4229: "MIDI Channel 6 Aftertouch",
    4230: "MIDI Channel 7 Aftertouch",
    4231: "MIDI Channel 8 Aftertouch",
    4232: "MIDI Channel 9 Aftertouch",
    4233: "MIDI Channel 10 Aftertouch",
    4234: "MIDI Channel 11 Aftertouch",
    4235: "MIDI Channel 12 Aftertouch",
    4236: "MIDI Channel 13 Aftertouch",
    4237: "MIDI Channel 14 Aftertouch",
    4238: "MIDI Channel 15 Aftertouch",
    4239: "MIDI Channel 16 Aftertouch",
}
