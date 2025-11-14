class Time:
    def set_time(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def show(self):
        print(f"{self.__h:02d}:{self.__m:02d}:{self.__s:02d}")

    def __add__(self, other):
        h = self.__h + other.__h
        m = self.__m + other.__m
        s = self.__s + other.__s

        if s >= 60:
            m += s // 60
            s = s % 60
        if m >= 60:
            h += m // 60
            m = m % 60

        t = Time()
        t.set_time(h, m, s)
        return t


# --- Main Program ---
t1 = Time()
t2 = Time()

print("Enter first time:")
t1.set_time(int(input("Hour: ")), int(input("Minute: ")), int(input("Second: ")))

print("\nEnter second time:")
t2.set_time(int(input("Hour: ")), int(input("Minute: ")), int(input("Second: ")))

t3 = t1 + t2

print("\nFirst Time: ", end="")
t1.show()
print("Second Time:", end=" ")
t2.show()
print("Sum of Times:", end=" ")
t3.show()

