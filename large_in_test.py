import time
from dtest import Tester, create_ks

class TestLarge(Tester):
    def test_large_in(self):
        self.cluster.populate(1)
        self.cluster.start(wait_for_binary_proto=True)
        node = self.cluster.nodelist()[0]
        session = self.patient_cql_connection(node)
        create_ks(session, "test", rf=1)
        session.execute("""CREATE TABLE users (id int PRIMARY KEY, name text)""")
        for i in range(10):
            tt = session.execute_async("select id from test.users where id in (%s)" % ','.join(map(str, range(100000))))
        print "attach jvm tool"
        time.sleep(1000)