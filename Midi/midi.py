import mido

print('List of in ports')
print(mido.get_input_names())

print('List of IO ports')
print(mido.get_ioport_names())

print('List of out ports')
print(mido.get_output_names())

'''
msg = mido.Message('note_on',note=60)
print(msg.note)
print(msg.bytes())
print(msg.copy(channel=2))
'''
outport = mido.open_output('Microsoft GS Wavetable Synth 0')

#outport = mido.open_output('CASIO USB-MIDI 2')
#outport = mido.open_output('Android 1')
outport.panic()
#with mido.open_input('CASIO USB-MIDI 1') as inport:
with mido.open_input('Android 0') as inport:
   for msg in inport:
      print(msg)  # Display message
      outport.send(msg)  # Play note

'''
# Midi File Functions

# Load MIDI file
mid = mido.MidiFile('abc.mid')

# Play MIDI file
for msg in mid.play():
    outport.send(msg)
    
# Print messages contained in the MIDI file

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
'''


'''
# Play Single Note
inport = mido.open_input('Android 0')
outport = mido.open_output('Microsoft GS Wavetable Synth 0')

msg = inport.receive()
outport.send(msg)
'''
