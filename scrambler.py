class Additive:
    def __init__(self, xor1, xor2, leng, seed):
        self.xor2 = leng - xor2 - 1
        self.seed = seed
        self.initseed = seed
        self.xor1 = leng - xor1 - 1
        self.leng = leng
        if self.xor1 < 0:
            self.xor1 = 0
        if self.xor2 < 0:
            self.sor2 = 0
        self.mod = 0
        for x in range(0, leng):
            self.mod = self.mod << 1
            self.mod += 1
        print(self.xor1, self.xor2, bin(self.seed), self.leng)
        self.syncseq = int("11111111", 2)
        self.currentseq = 0

    def scramble(self, data):
        help = 0
        truebyte = int("11111111", 2)
        for x in range(0, 8):
            help = ((self.seed >> self.xor1) ^ (self.seed >> self.xor2)) << 7 | help >> 1
            help = help & truebyte
            self.seed = self.seed >> 1 | (((self.seed >> self.xor1) ^ (self.seed >> self.xor2)) << (self.leng-1))
            self.seed = self.seed & self.mod
            self.currentseq = (self.currentseq >> 1 | (data >> x & 1) << 7 & truebyte)
            if self.currentseq == self.syncseq:
                self.initialState()
        data = data ^ help
        return data

    def scrambleOneX(self, data):
        help = 0
        truebyte = int("11111111", 2)
        for x in range(0, 8):
            help = (self.seed >> self.xor1) << 7 | help >> 1
            help = help & truebyte
            self.seed = self.seed >> 1 | ((self.seed >> self.xor1) << (self.leng-1))
            self.seed = self.seed & self.mod
            self.currentseq = (self.currentseq >> 1 | (data >> x & 1) << 7 & truebyte)
            if self.currentseq == self.syncseq:
                self.initialState()
        data = data ^ help
        return data

    def initialState(self):
        self.seed = self.initseed
        self.currentseq = 0


class Multiplicative:
    def __init__(self, xor1, xor2, leng, seed):
        self.xor2 = leng - xor2 - 1
        self.seed = seed
        self.initseed = seed
        self.xor1 = leng - xor1 - 1
        self.leng = leng
        if self.xor1 < 0:
            self.xor1 = 0
        if self.xor2 < 0:
            self.sor2 = 0
        self.mod = 0
        for x in range(0, leng):
            self.mod = self.mod << 1
            self.mod += 1
        print(self.xor1, self.xor2, bin(self.seed), self.leng)

    def scrambleIn(self, data):
        truebyte = int("11111111", 2)
        for x in range(0, 8):
            self.seed = self.seed >> 1 | ((((self.seed >> self.xor1) ^ (self.seed >> self.xor2)) ^ data) << (self.leng - 1))
            self.seed = self.seed & self.mod
            data = (self.seed >> (self.leng - 1)) << 7 | data >> 1
            data = data & truebyte

        return data

    def scrambleInOneX(self, data):
        truebyte = int("11111111", 2)
        for x in range(0, 8):
            self.seed = self.seed >> 1 | (((self.seed >> self.xor1) ^ data) << (self.leng - 1))
            self.seed = self.seed & self.mod
            data = (self.seed >> (self.leng - 1)) << 7 | data >> 1
            data = data & truebyte

        return data

    def scrambleOut(self, data):
        truebyte = int("11111111", 2)
        for x in range(0, 8):
            self.seed = self.seed | data << self.leng
            data = (((self.seed >> self.xor1) ^ (self.seed >> self.xor2)) ^ data) << 7 | data >> 1
            self.seed = self.seed >> 1 & self.mod
            data = data & truebyte
        return data
    def scrambleOutOneX(self, data):
        truebyte = int("11111111", 2)
        for x in range(0, 8):
            self.seed = self.seed | data << self.leng
            data = ((self.seed >> self.xor1) ^ data) << 7 | data >> 1
            self.seed = self.seed >> 1 & self.mod
            data = data & truebyte
        return data

    def initialState(self):
        self.seed = self.initseed
