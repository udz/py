import mido

print('List of in ports')
print(mido.get_input_names())

print('List of IO ports')
print(mido.get_ioport_names())

print('List of out ports')
print(mido.get_output_names())


mido.write_syx_file
# Midi File Functions

# Load MIDI file
outport = mido.open_output('Microsoft GS Wavetable Synth 0')
#outport = mido.open_output('CASIO USB-MIDI 1')
#outport = mido.open_output('Android 1')

outport.panic()
#mid = mido.MidiFile('abc.mid')
mid = mido.MidiFile('Ace_of_Base_-_All_That_She_Wants.mid')

# Play MIDI file
for msg in mid.play():
    outport.send(msg)
    
# Print messages contained in the MIDI file
'''
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
'''
