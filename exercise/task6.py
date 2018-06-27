'''
Provided a text file with information about artists and songs:
Joy Division - Love Will Tear Us Apart
Joy Division - New Dawn Fades
Pixies - Where Is My Mind
Pixies - Hey
Genesis - Mama
Write the required classes so the following code works:

music = MusicFile('/Users/ynonperek/music.txt')
print(music.artist('Joy Division').songs)
'''
class MusicFile(object):
    def __init__(self,path_file):
        with open(path_file,'r') as file:
            self.content = file.readlines()        
        #return self.file
    def artist(self,artist_name):
        #print(self.content)
        for line in self.content:
            #if line.__contains__(artist_name):
            if artist_name in line:
                print(line)

music = MusicFile('exercise\music.txt')

print(music.artist('Joy Division'))

'''
with MusicFile('exercise\music.txt') as music2:
    print(music2.artist('Pixies'))
'''