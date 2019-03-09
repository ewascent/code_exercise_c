"""import a small or large array of repeating vals"""
from asyncio import get_event_loop, wait
from sys import getrecursionlimit, setrecursionlimit
from src.recursive_repeater import repeater_recurse as repeater
from src.xml_parser import getText, fetchData, xmlReader

Vals = list(range(1, 5000))#[1, 2, 3, 4, 1, 2, 3]

async def main(vals, loop):
    """entry point for application. takes an array of ints"""
    before = getrecursionlimit()

    task2 = loop.create_task(setrecursionlimit(15000))
    task3 = loop.create_task(print("==Run the repeater code.== \n"))
    task4 = loop.create_task(print("This should be 1 -> " + str(repeater(vals)) + "\n"))
    task5 = loop.create_task(print("==Parse some XML== \n" + getText(fetchData('http://slashdot.org/slashdot.rdf'))))
    task6 = loop.create_task(print(xmlReader(fetchData('http://slashdot.org/slashdot.rdf'), 200, 200)))
    task_list = [task2, task3, task4, task5, task6]
    await wait(task_list)
    setrecursionlimit(before)

if __name__ == "__main__":
    try:
        event_loop = get_event_loop()
        event_loop.run_until_complete(wait(print(main(Vals, event_loop))))
    except Exception as e:
        print("ERROR - Main method " + str(e))
        raise e
    finally:
        event_loop.close()
