x = 52 # The seed value for the pseudo-random sequence

for n in range(0, 100):
    print(x % 100)
    x = (12553*x+15401)%6133
