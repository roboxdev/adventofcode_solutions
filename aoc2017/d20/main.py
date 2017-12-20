import re
from operator import itemgetter

from aocframework import AoCFramework

MAGIC_STABILITY_REFERENCE = 1000  # Hope that's enough


class Day(AoCFramework):
    test_cases = (
        ('''p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>''', 0),
)

    def find_closest(self, particles):
        return min(((i, sum(tuple(map(abs, p)))) for i, (p, *_) in enumerate(particles)), key=itemgetter(1))[0]

    def tick(self, particles):
        new_particles = []
        for p, v, a in particles:
            new_v = tuple(map(sum, zip(v, a)))
            new_p = tuple(map(sum, zip(new_v, p)))
            particle = (new_p, new_v, a)
            new_particles.append(particle)
        return new_particles

    def go(self):
        closest = None
        stability_counter = 0
        particles = []
        pattern = r'p=< ?(?P<px>.+),(?P<py>.+),(?P<pz>.+)>, v=< ?(?P<vx>.+),(?P<vy>.+),(?P<vz>.+)>, a=< ?(?P<ax>.+),(?P<ay>.+),(?P<az>.+)>'
        for b in self.linesplitted:
            match = re.match(pattern, b)
            assert match
            d = match.groupdict()
            particles.append((
                (int(d['px']), int(d['py']), int(d['pz'])),
                (int(d['vx']), int(d['vy']), int(d['vz'])),
                (int(d['ax']), int(d['ay']), int(d['az'])),
            ))
        while True:
            particles = self.tick(particles)
            new_closest = self.find_closest(particles)
            if closest == new_closest:
                stability_counter += 1
                if stability_counter >= MAGIC_STABILITY_REFERENCE:
                    return closest
            else:
                closest = new_closest
                stability_counter = 0

Day()
