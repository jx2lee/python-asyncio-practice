import sys
from restaurant.threadbot import ThreadBot, Cutlery


def tableware_object_definition():
    kitchen = Cutlery(knives=100, forks=100)
    bots = [ThreadBot(kitchen) for _ in range(10)]

    for bot in bots:
        for i in range(int(sys.argv[1])):
            bot.tasks.put('prepare table')
            bot.tasks.put('clear table')
        bot.tasks.put('shutdown')

    print('Kitchen inventory before service: ', kitchen)
    for bot in bots:
        bot.start()

    for bot in bots:
        bot.join()
    print('Kitchen inventory after service: ', kitchen)


if __name__ == '__main__':
    tableware_object_definition()
    # 식탁(인자)이 100개 인 경우 문제 없지만
    # 10000개인 경우 context switch 로 인해 100개 knife & fork 를 반납 해야 하지만, 그렇지 못하다.
    # 단 하나의 ThreadBot 을 사용해 모든 식탁을 처리 하도록 하는 것 (kitchen 변수의 칼과 포크를 하나의 스레드에 의해 수정되도록 하는 것)