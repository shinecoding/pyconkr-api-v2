# Generated by Django 4.1.5 on 2023-02-11 15:16

from django.db import migrations, models
import sponsor.models


class Migration(migrations.Migration):

    dependencies = [
        ("sponsor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsor",
            name="bank_book_file",
            field=models.FileField(
                blank=True,
                help_text="후원사 사업자 등록증 스캔본입니다. 세금 계산서 발급에 사용됩니다.",
                null=True,
                upload_to=sponsor.models.bank_book_file_upload_to,
            ),
        ),
        migrations.AddField(
            model_name="sponsor",
            name="manager_tel",
            field=models.CharField(
                default="",
                help_text="메일에 회신이 없거나, 긴급한 건의 경우, 문자나 유선으로 안내드릴 수 있습니다. 후원 담당자의 유선 연락처를 입력해주십시오.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="business_registration_file",
            field=models.FileField(
                blank=True,
                default=None,
                help_text="후원사 사업자 등록증 스캔본입니다. 세금 계산서 발급에 사용됩니다.",
                null=True,
                upload_to=sponsor.models.registration_file_upload_to,
            ),
        ),
    ]
