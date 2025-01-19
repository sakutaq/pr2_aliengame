class Settings():

    def __init__(self):
        
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        self.ship_speed = 0.1
        self.ship_limit = 3

        self.bullet_speed = 0.06
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.alien_speed = 0.05
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 
        