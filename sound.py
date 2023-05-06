from setting import *

pygame.mixer.init()
pygame.mixer.music.load(os.path.join("assest", "music12.mp3"))
pygame.mixer.music.play(loops=1)

# load all sound files

move_left = pygame.mixer.Sound(os.path.join("assest", "move_r.mp3"))
move_right = pygame.mixer.Sound(os.path.join("assest", "move_r.mp3"))
collect_sound = pygame.mixer.Sound(os.path.join("assest", "collect.mp3"))
