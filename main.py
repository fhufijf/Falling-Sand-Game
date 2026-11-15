import pygame, sys, asyncio
from simulation import Simulation

async def main():
    pygame.init()
    pygame.mouse.set_visible(False)

    window_width = 800
    window_height = 600
    cell_size = 5
    fps = 120
    grey = (29, 29, 29)

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Falling Sand")

    clock = pygame.time.Clock()
    simulation = Simulation(window_width, window_height, cell_size)

    while True: 

        simulation.handle_controls()

        simulation.update()

        window.fill(grey)
        simulation.draw(window)

        pygame.display.flip()
        clock.tick(fps)

        await asyncio.sleep(0)

asyncio.run(main())