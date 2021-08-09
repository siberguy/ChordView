

numfrets=13
#numstrings=6
#banjo=0

# Identify the intervals 

UNISON =        0o4000
M_SECOND =      0o2000
SECOND =        0o1000
M_THIRD =       0o0400
THIRD =         0o0200
FOURTH =        0o0100
TRITONE =       0o0040
FIFTH =         0o0020
M_SIXTH =       0o0010
SIXTH =         0o0004
M_SEVENTH =     0o0002
SEVENTH =       0o0001

CHROMATIC =     0o7777


chords = { 'major':      (UNISON|THIRD|FIFTH),
           'minor':      (UNISON|M_THIRD|FIFTH),
           'narural minor':        (UNISON|SECOND|M_THIRD|FOURTH|FIFTH|M_SIXTH|M_SEVENTH),
           'melodic minor':        (UNISON|SECOND|M_THIRD|FOURTH|FIFTH|SIXTH|SEVENTH),
           'whole tone':        (UNISON|SECOND|THIRD|TRITONE|M_SIXTH|M_SEVENTH),
           'altered':    (UNISON|M_SECOND|M_THIRD|THIRD|TRITONE|M_SIXTH|M_SEVENTH),
           'aug':        (UNISON|THIRD|M_SIXTH),
           'diminished': (UNISON|M_THIRD|TRITONE),       
           '7':          (UNISON|THIRD|FIFTH|M_SEVENTH),
           'maj7':       (UNISON|THIRD|FIFTH|SEVENTH),
           'm7':         (UNISON|M_THIRD|FIFTH|M_SEVENTH),
           'm9':         (UNISON|M_THIRD|FIFTH|M_SEVENTH|SECOND),
           'dim7':       (UNISON|M_THIRD|TRITONE|SIXTH),        
           'sus':        (UNISON|FOURTH|FIFTH),
           'add9':       (UNISON|THIRD|FIFTH|SECOND),
           '9':          (UNISON|THIRD|FIFTH|M_SEVENTH|SECOND),
           'm7b5':       (UNISON|M_THIRD|TRITONE|M_SEVENTH),
           '7b5':        (UNISON|THIRD|TRITONE|M_SEVENTH),
           '7#5':        (UNISON|THIRD|M_SIXTH|M_SEVENTH),
           '7#9':        (UNISON|THIRD|FIFTH|M_SEVENTH|M_THIRD),
           '7b9':        (UNISON|THIRD|FIFTH|M_SEVENTH|M_SECOND),
           '6':          (UNISON|THIRD|FIFTH|SIXTH),
           '13':         (UNISON|THIRD|SIXTH|M_SEVENTH),
           '6/9':        (UNISON|THIRD|SIXTH|SECOND),
           'aug':        (UNISON|THIRD|M_SIXTH),
           '7 gtones':          (THIRD|M_SEVENTH),
           'maj gtones7':       (THIRD|SEVENTH),
           'm7 gtones':         (M_THIRD|M_SEVENTH),
           'tab':        (0)
}

chord_order = ['major',
           'minor',
           'narural minor',
           'melodic minor',
           'altered',
           'aug',
           'diminished',
           'whole tone',
           '7',
           'maj7',
           'm7',
           'm9',
           'dim7',
           'sus',
           'add9',
           '9',
           'm7b5',
           '7b5',
           '7#5',
           '7#9',
           '7b9',
           '6',
           '13',
           '6/9',
           'aug',
           '7 gtones',
           'maj gtones7',
           'm7 gtones',
           'tab'
]
keys = { 'C'  : 0,
         'Db' : 1,
         'D'  : 2,
         'Eb' : 3,
         'E'  : 4,
         'F'  : 5,
         'Gb' : 6,
         'G'  : 7,
         'Ab' : 8,
         'A'  : 9,
         'Bb' : 10,
         'B'  : 11 
}

keys_inv = { 0  : 'C',
             1  : 'Db',
             2  : 'D',
             3  : 'Eb',
             4  : 'E',
             5  : 'F',
             6  : 'Gb',
             7  : 'G',
             8  : 'Ab',
             9  : 'A',
             10 : 'Bb',
             11 : 'B',
}

tunings = { "Standard" : ["E","B","G","D","A","E"],
            "DADGAD" : ["D","A","G","D","A","D"],
            "Open G" : ["D","B","G","D","G","D"],
            "Open D" : ["D","A","F#","D","A","D"],
            "Banjo G" : ["D","B","G","D","G"],
            "Banjo Sawmill" : ["D","C","G","D","G"],
            "Banjo Double C" : ["D","C","G","C","G"],
            "Banjo Loretta" : ["C","Bb","F","C","Eb"],
            "Lap Steel " : ["D","A","F#","D","B","G"],
            "Lap Steel A " : ["D","B","F#","D","B","G"],
            "Lap Steel B " : ["D","A","G","D","B","G"],
            "Lap Steel AB " : ["D","B","G","D","B","G"],
            "Lap Steel C " : ["Db","A","F#","D","B","G"],
            "Lap Steel BC " : ["Db","A","G","D","B","G"]
          }

tuning_dict = {  'C' : 36,
                 'C#' : 37,
                 'Db' : 37,
                 'D' : 38,
                 'D#' : 39,
                 'Eb' : 39,
                 'E' : 40,
                 'F' : 41,
                 'F#' : 42,
                 'Gb' : 42,
                 'G' : 43,
                 'G#' : 44,
                 'Ab' : 44,
                 'A' : 45,
                 'A#' : 46,
                 'Bb' : 46,
                 'B' : 47,
}

tuning = [40,47,43,38,45,40]
tuning_note = ["E","B","G","D","A","E"]
#tuning = [40,45,50,55,59,64]


basenote = [ 0, 2, 3, 5, 7, 8, 10 ]
sharpnames = ['A','A','B','C','C','D','D','E','F','F','G','G']
flatnames  = ['A','B','B','C','D','D','E','E','F','G','G','A']




def inmask(i,m):
         r  = ((1 << (11-(i))) & (m))
         if(r == 0):
               return 0
         else:
               return 1
#         return (!!((1 << (11-(i))) & (m)))


def transp(k,m):
#        r = (((m) << (12-(k))) & CHROMATIC | ((unsigned)(m) >> (k)))
         r = (((m) << (12-(k))) & CHROMATIC | ((m) >> (k)))
         return r

def fret_note(s,f,bnjo):
        # fix 5th string
        off=-5
        if bnjo >0 and s == 4:
             return tuning[s] + f +off
        else:
             return tuning[s] + f


def notenum(n,o):
         return (12*((o)-1)+(n))

def octave(nn):
         return ((nn)/12+1)

def octvnote(nn):
         return ((nn)%12)






def get_note(s,f,k,c,numstrings,bnjo):
        #print("s ",s)
        #print("f ",f)
        #print("k ",k)
        #print("c ",c)
        sharp=0
        shownotes=0
        str_ret = ' '
        default = -999
#       print "key,chord 2 ",k,c
        mask = chords.get(c,default)
        if(mask == -999):
#           print 'Bad chord name',c
            return
#       print 's,f,mask = ',s,f,mask

        default_key = 0  
        key = keys.get(k,default_key)
#       print 'key = ',key
        mask2 = transp(key,mask)
#       print 'mask2 = ',mask2

        local_note = fret_note(s,f,bnjo);
#       print 'local_note = ',local_note
        onote = octvnote(local_note);
#       print '1 onote = ',onote

        sw = inmask(onote,mask2) 
#       print 'switch  = ',sw

        if(sw): 
              n = (local_note + 3) % 12;  
#             print 'n  = ',n
              str_ret = sharpnames[n]              
#             print 'str_ret  = ',str_ret
              for l in range(0, numstrings):
                        if(basenote[l] == n):
                                   sharp=0;
              if(sharp):
                    str_ret = str_ret+'#'
           
              if(shownotes):
                    notenamein=str_ret
              else:
                    onote = onote - key
#             print '2 onote = ',onote
              if(onote < 0):
                    onote = onote+12;
              onote = onote + 1
#             print 'onote = ',onote
              if(onote < 10):
                notenamein=' ' + str(onote);
              else:
                notenamein=str(onote);
#             print 'notenamein = ',notenamein
              
              if(onote == 2):
                        notenamein="b9"
              elif(onote == 3):
                        notenamein=" 9"
              elif(onote == 4):
                        notenamein="b3"
              elif(onote == 5):
                        notenamein=" 3"
              elif(onote == 6):
                        notenamein=" 4"
              elif(onote == 7):
                        notenamein="b5"
              elif(onote == 8):
                        notenamein=" 5"
              elif(onote == 9):
                        notenamein="#5"
              elif(onote == 10):
                        notenamein=" 6"
              elif(onote == 11):
                        notenamein="b7"
              elif(onote == 12):
                        notenamein=" 7"
        else:
              notenamein=""


#       print 'returned notenamein = ',notenamein
#       print '-  '
#       print '-  '
        return notenamein











