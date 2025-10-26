def przeksztalc(dane):
  for i in range(len(dane)):
    if i % 2 == 0: # N
      dane[i] *= 2 # N/2
    else:
      dane[i] /= 2 # N/2

# T(N) = 2N
# O(N) = N

def przeksztalc_v2(dane):
  for i in range(0, len(dane), 2):
    dane[i] *= 2 # N/2
  for i in range(1, len(dane), 2):
    dane[i] /= 2 # N/2

# T(N) = N
# O(N) = N



dane = [3, 7, 9, 12, 19, 30, 41, 56, 71]
przeksztalc(dane)
print(dane)










