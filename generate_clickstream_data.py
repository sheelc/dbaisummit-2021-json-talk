import json
import random
import secrets

from datetime import datetime

from faker import Faker

EVENTS = ['pageview', 'link_click', 'scroll', 'mouse_move']

Faker.seed(0)
fake = Faker()
f = open("clickstream_full.json", "w+")
for _ in range(1000):
    ts = fake.date_time_this_decade()
    event = random.choice(EVENTS)
    event = {
        'event_ts': ts.isoformat(),
        'event': event,
        'device': {
            'browser_id': secrets.token_urlsafe(8),
            'ip': fake.ipv4(),
            'user_agent': fake.user_agent()
        }
    }

    if ts >= datetime(2020, 12, 21):
        del event['device']['ip']
    if ts <= datetime(2020, 6, 2):
        event['device']['browser_id'] = random.randint(10000, 10000000)

    f.write(json.dumps(event))
    f.write('\n')
f.close()