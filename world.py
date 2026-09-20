from dataclasses import dataclass, field


@dataclass
class Event:
    day: int
    time: str
    description: str


@dataclass
class World:
    day: int = 1
    time: str = "08:00"
    events: list[Event] = field(default_factory=list)

    def add_event(self, description: str):
        event = Event(
            day=self.day,
            time=self.time,
            description=description
        )

        self.events.append(event)

    def show_history(self):
        for event in self.events:
            print(
                f"Day {event.day} [{event.time}] "
                f"{event.description}"
            )
