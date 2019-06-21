class TowersOfHanoi():
    def __init__(self, n):
       rod1 = []
       rod2 = []
       rod3 = []
       self.rods = [rod1, rod2, rod3]
       self.n = 0

    def moveDisk(self, stardingIndex, destinationIndex):
        popped = self.rods[stardingIndex].pop()
        self.rods[destinationIndex].append(popped)

    def addDisk(self, disk, rodIndex):
        self.rods[rodIndex].append(disk)
        self.n += 1

    def disksAtRod(self, index):
        list = []
        for e in self.rods[index]:
            list.append(e)
        return list


    def playGame(self, n, starting, destination, other):
        if n == 1:
            self.moveDisk(starting, destination)
            return
        self.playGame(n - 1, starting, other, destination) #move everything  at the top over
        self.moveDisk(starting, destination) #move that one disk
        self.playGame(n - 1, other, destination, starting)#move everything else back where that one disk went

def main():
    return


if __name__ == '__main__':
    main()