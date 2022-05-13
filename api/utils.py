import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

def create_random_plate():
    N1 = random.choice(numbers)
    N2 = random.choice(numbers)
    #generate 4 randomly chosen numbers, N1, N2, N3, N4
    L1 = random.choice(letters)
    L2 = random.choice(letters)
    L3 = random.choice(letters)

    N3 = random.choice(numbers)
    N4 = random.choice(numbers)

    return N1+N2+' '+L1+L2+L3+' '+N3+N4


def latest_records():
    now = timezone.now()
    # vehicle = Vehicle.objects.filter(id=15).first()
    # for i in range(20):
    #     past = now - datetime.timedelta(seconds=random.randint(0, 10*86400))
    #     record = NavigationRecord.objects.create(vehicle=vehicle, latitude=round(random.uniform(1,50), 2), longitude=round(random.uniform(1,50), 2), datetime=past)
    #     record.save()
    last2days = now - datetime.timedelta(seconds=random.randint(0, 2*86400))
    print("---------------------------")
    print(NavigationRecord.objects.annotate(plate="vehicle"))
    print("---------------------------")
    query_set = NavigationRecord.objects.filter(datetime__range = [last2days, now])
    # query_set_formatted = query_set.annotate(formatted_date=Func(F('datetime'), Value('DD.MM.YYYY HH:MM:ss'), function='to_char', output_field=CharField()))
    return query_set