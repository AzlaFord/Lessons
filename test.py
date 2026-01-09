import cv2
import time

img = cv2.imread("vandam.png")
assert img is not None

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
assert not face.empty()

# precompute gray (Test A)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def bench(fn, iters=200, warmup=20):
    for _ in range(warmup):
        fn()
    t0 = time.perf_counter()
    for _ in range(iters):
        fn()
    t1 = time.perf_counter()
    return (t1 - t0) / iters * 1000  # ms/iter


# A) gray pregătit o dată
t_A = bench(lambda: face.detectMultiScale(gray, 1.1, 5), iters=200, warmup=20)

# B) convertesc la fiecare iterație + detect
t_B = bench(lambda: face.detectMultiScale(cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY), 1.1, 5), iters=200, warmup=20)

print(f"A) detect pe gray precomputat: {t_A:.3f} ms/iter")
print(f"B) gray+detect (gray recalculat): {t_B:.3f} ms/iter")
print(f"Cost conversie (aprox): {t_B - t_A:.3f} ms/iter")
