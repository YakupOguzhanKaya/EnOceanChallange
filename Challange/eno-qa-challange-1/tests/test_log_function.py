from log_function import log_to_stdout
import unittest
import asyncio


class Test_Challenge_3(unittest.TestCase):
    timeout_value = 70

    def test_challenge_3(self):
        loop = asyncio.get_event_loop()
        with self.assertLogs() as captured:
            loop.create_task(log_to_stdout())
            loop.run_until_complete(self.timer())
            self.assertEqual(len(captured.records), (self.timeout_value // 60) + 1)
            for i in range(len(captured.records)):
                self.assertEqual(captured.records[i].getMessage(),
                                 "This line should be logged every 1 minute")

    async def timer(self):
        await asyncio.sleep(self.timeout_value)


if __name__ == '__main__':
    unittest.main()
