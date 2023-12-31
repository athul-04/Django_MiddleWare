# Generated by Django 4.1.3 on 2022-11-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_users_private_key_users_public_key"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="users",
            name="email",
        ),
        migrations.RemoveField(
            model_name="users",
            name="name",
        ),
        migrations.AlterField(
            model_name="users",
            name="private_key",
            field=models.TextField(
                default=b"-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDJmxOe4ig73NhC8BukOVCa0kQckBz3pBihmrfsLhwEh2GLuSc+\n1m+nKsJWwS5uGNLgNezFG9Jp5eBNTek7jloDXcLR6XT2CwSZSz7Ez4UPbAZLrRSg\n2H4jSpQm3WPLvhlRzaxv4APtKaXTpL7Yctbf8KUlp+g6DBlMmNEXQZsRAwIDAQAB\nAoGAVy2nfN+X/Vbg74UrtsaQC/rbuCw7UnzTp+IjIU7JD85JCKX+igYpTvTHB8PO\no445dfnrkkqXIPLmHReRQQ8r7Z45j7xB9Pxtm2WWJGegeXHwCB81jYGO+kPcwJ+z\naIJMTyTrQ7+sf09/3yQS8Sp7fMfUYtVj0XyLnx0aIyIOVDUCQQDNNW9rrRycVAI+\n3W7p1ILQ2PjTaGfFSCFrayCi3CfKKxzJqJxDpn9o+lMzrrzexBLNrc0RBhzjyr69\nPsJaEI5lAkEA+4FZImp0wclbQnCXyKz51VxlURZV4+5ArpC30LRBECpyRMREP3fv\n6fNZ/w1zI57kbkDCKM5nf5qdAlOre46XRwJAVpfQ36gaJaGRnQOF1Sg213hnb5Zk\nC6zHZXO8Pt0V8UrGCBadcjKlGyBe0bVPv9UPdjl8Ck4BDOK2IFeGXckUvQJAClmb\nWnA5F9R6ffR2OprruR0RSlH5/ORMIyLvfZY9azXj9/J/wIDmDaGnHXjnORsL2YGu\nu9EqrzSkq3jYAMCwdwJBAIMdFZXFEZWuiCmR7xjQbhya5ckhF3XdUlllEd2MYlIK\nk8VcfUpxo38hBS4KxLFKOdjCN4csPt4l7GrnkAyeBk4=\n-----END RSA PRIVATE KEY-----"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="public_key",
            field=models.TextField(
                default=b"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDJmxOe4ig73NhC8BukOVCa0kQc\nkBz3pBihmrfsLhwEh2GLuSc+1m+nKsJWwS5uGNLgNezFG9Jp5eBNTek7jloDXcLR\n6XT2CwSZSz7Ez4UPbAZLrRSg2H4jSpQm3WPLvhlRzaxv4APtKaXTpL7Yctbf8KUl\np+g6DBlMmNEXQZsRAwIDAQAB\n-----END PUBLIC KEY-----"
            ),
        ),
    ]
