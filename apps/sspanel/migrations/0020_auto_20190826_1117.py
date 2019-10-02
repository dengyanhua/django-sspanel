# Generated by Django 2.2.1 on 2019-08-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0019_auto_20190826_0950")]

    operations = [
        migrations.AddField(
            model_name="usertrafficlog",
            name="node_type",
            field=models.CharField(
                choices=[("ss", "ss"), ("vmess", "vmess")],
                default="ss",
                max_length=32,
                verbose_name="节点类型",
            ),
        ),
        migrations.AlterField(
            model_name="nodeonlinelog",
            name="node_type",
            field=models.CharField(
                choices=[("ss", "ss"), ("vmess", "vmess")],
                default="ss",
                max_length=32,
                verbose_name="节点类型",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="sub_type",
            field=models.SmallIntegerField(
                choices=[(0, "只订阅SS"), (1, "只订阅Vmess"), (2, "订阅所有")],
                default=2,
                verbose_name="订阅类型",
            ),
        ),
        migrations.AlterIndexTogether(
            name="usertrafficlog",
            index_together={("user_id", "node_type", "node_id", "date")},
        ),
    ]