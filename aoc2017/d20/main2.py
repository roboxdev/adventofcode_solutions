import re
from operator import itemgetter

from aocframework import AoCFramework

MAGIC_STABILITY_REFERENCE = 1000  # Hope that's enough


class Day(AoCFramework):
    test_cases = (
        ('''p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>''', 1),
    )

    def remove_collisions(self, particles):
        new_particles = []
        collisions = []
        for particle in particles:
            if particle[0] not in tuple(map(itemgetter(0), new_particles)):
                new_particles.append(particle)
            else:
                collisions.append(particle[0])
        new_particles = list(filter(lambda v: v[0] not in collisions, new_particles))
        return new_particles

    def tick(self, particles):
        new_particles = []
        for p, v, a in particles:
            new_v = tuple(map(sum, zip(v, a)))
            new_p = tuple(map(sum, zip(new_v, p)))
            particle = (new_p, new_v, a)
            new_particles.append(particle)
        without_collisions = self.remove_collisions(new_particles)
        return without_collisions

    def go(self):
        answer = None
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
            new_answer = len(particles)
            if answer == new_answer:
                stability_counter += 1
                if stability_counter >= MAGIC_STABILITY_REFERENCE:
                    return answer
            else:
                answer = new_answer
                stability_counter = 0

Day()
