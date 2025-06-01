# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    province = models.BigIntegerField(blank=True, null=True, verbose_name='استان/شهر')

    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'AUTH_USER'

class AccActivePerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey('AccInspection', models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    active_person = models.IntegerField(db_comment='��� ��� :�������=0� �������=1')
    first_name = models.CharField(max_length=255, blank=True, null=True, db_comment='���')
    last_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �����ϐ�')
    national_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�� ���')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='����')
    logical_delete = models.BooleanField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �ј�')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    fulll_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� ����')

    class Meta:
        managed = False
        db_table = 'acc_active_person'
        db_table_comment = '������� ������� � �������(�������)'


class AccActivePersonReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('AccInspectorReport', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    active_person = models.IntegerField(db_comment='��� ��� :�������=0� �������=1')
    first_name = models.CharField(max_length=255, db_comment='���')
    last_name = models.CharField(max_length=255, db_comment='��� �����ϐ�')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    national_code = models.CharField(max_length=10, blank=True, null=True, db_comment='�� ���')
    phone = models.CharField(max_length=11, db_comment='����')
    company_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �ј�')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_active_person_report'
        db_table_comment = '������� ������ǡ �������(�����)'


class AccArchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.BigIntegerField(db_comment='����� �������')
    createdby = models.BigIntegerField()
    letter_number = models.CharField(max_length=20, db_comment='����� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True, db_comment='�������')

    class Meta:
        managed = False
        db_table = 'acc_archive'
        db_table_comment = '������ ������'


class AccBylawsReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.BigIntegerField(db_comment='����� �����')
    bylaws = models.BigIntegerField(db_comment='����� ���� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_bylaws_report'
        db_table_comment = '���� ���� ��� ��� ���'


class AccDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey('AccInspection', models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    file_type = models.BigIntegerField(db_comment='����� ��� ����')
    injured = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile', db_comment='����� ���')
    tracking_code = models.CharField(max_length=255, db_comment='����� ���')
    logical_delete = models.BooleanField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_document'
        db_table_comment = '������� �������'


class AccDocumentReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('AccInspectorReport', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� �����')
    filetype = models.BigIntegerField(db_comment='����� ��� ����')
    injured = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile', db_comment='����� ���')
    trackingcode = models.CharField(max_length=255, db_comment='����� ���')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_document_report'
        db_table_comment = '������� �����'


class AccInjured(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey('AccInspection', models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    accident_result = models.IntegerField(db_comment='����� �����: ��� 0� ������ 1')
    agent_type = models.BigIntegerField(blank=True, null=True, db_comment='����� ��� ���� �����')
    education_degree = models.BigIntegerField(blank=True, null=True, db_comment='����� �������')
    fida_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�� ��ǐ�� �����')
    gender = models.BigIntegerField(db_comment='�����')
    is_educated = models.BooleanField(blank=True, null=True, db_comment='��� ���� � ����� ���� ��ʿ')
    job = models.CharField(max_length=4000, db_comment='����� ���� ��� ����� ����')
    job_history = models.IntegerField(db_comment='����� ��ѐ� �� ��� (���)')
    last_name = models.CharField(max_length=255, db_comment='��� �����ϐ�')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, db_comment='���')
    national_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�� ���')
    nationality = models.IntegerField(db_comment='����: ������ 01� ��� ������ 02')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='����')
    workshop_history = models.IntegerField(db_comment='����� ��ѐ� �� ��ѐ�� (���)')
    logical_delete = models.BooleanField(blank=True, null=True)
    action = models.CharField(max_length=4000, db_comment='�� ������ �� ��� ���� �����')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_injured'
        db_table_comment = '������ ����� ��ϐ�� (�������)'


class AccInjuredBodyPart(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    version = models.BigIntegerField()
    injured = models.BigIntegerField(db_comment='����� ����� ����')
    createdby = models.BigIntegerField()
    createdat = models.DateTimeField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    logical_delete = models.BooleanField()
    parent_body_part = models.BigIntegerField(db_comment='����� ��� ���� ���� (����)')
    sub_body_part = models.BigIntegerField(db_comment='����� ��� ���� ���� (��ѐ���)')

    class Meta:
        managed = False
        db_table = 'acc_injured_body_part'
        db_table_comment = '���� ���� ��ϐ�� (�������)'


class AccInjuredReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('self', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� �����')
    accident_result = models.IntegerField(db_comment='����� �����')
    age = models.IntegerField(db_comment='��')
    agent_type = models.BigIntegerField(blank=True, null=True, db_comment='����� ���� �� ��ѐ��(�������-�������)')
    fida_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�� ����')
    first_name = models.CharField(max_length=255, db_comment='���')
    gender = models.BigIntegerField(db_comment='�����')
    insurance_status = models.BooleanField(blank=True, null=True, db_comment='����� ����')
    job_history = models.IntegerField(blank=True, null=True, db_comment='����� ���')
    last_name = models.CharField(max_length=255, db_comment='��� �����ϐ�')
    marital_status = models.BigIntegerField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    national_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�� ���')
    nationality = models.IntegerField(db_comment='����')
    phone = models.CharField(max_length=255, db_comment='����')
    safety_equipment = models.BigIntegerField(blank=True, null=True, db_comment='������� �����')
    total_wages = models.BigIntegerField(db_comment='���� � ������')
    workshop_history = models.IntegerField(db_comment='����� ��ѐ��')
    workshop_shift = models.BigIntegerField(blank=True, null=True, db_comment='���� ����')
    graduation_level = models.BigIntegerField(db_comment='����� �������')
    injured_body_description = models.CharField(max_length=4000, blank=True, null=True, db_comment='����� ����� ����')
    action_description = models.CharField(max_length=4000, blank=True, null=True, db_comment='������� ������')
    sub_job = models.BigIntegerField(db_comment='��� ���� ���')
    action = models.BigIntegerField(db_comment='������')
    job = models.CharField(max_length=255, db_comment='���')
    is_educated = models.BooleanField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_injured_report'
        db_table_comment = '������ ����� ��ϐ�� (�����)'


class AccInjuredReportBodyPart(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField()
    injured = models.BigIntegerField(db_comment='����� ����� ����')
    logical_delete = models.BooleanField()
    parent_body_part = models.BigIntegerField(db_comment='����� ��� ���� ���� (����)')
    sub_body_part = models.BigIntegerField(db_comment='����� ��� ���� ���� (��ѐ���)')

    class Meta:
        managed = False
        db_table = 'acc_injured_report_body_part'
        db_table_comment = '���� ���� ��ϐ�� (�����)'


class AccInspection(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_date = models.DateTimeField(db_comment='����� �����')
    accident_place = models.BigIntegerField(db_comment='��� �����')
    has_media = models.BooleanField(db_comment='��� ���� �� ژ� ���� ���Ͽ')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    person_injured_count = models.IntegerField(db_comment='����� ����� ����� ����')
    reporter_other_position = models.CharField(max_length=4000, blank=True, null=True, db_comment='����� ��� ����� �����(����)')
    reporter_position = models.BigIntegerField(db_comment='��� ��� ����� �����')
    step = models.CharField(max_length=255, db_comment='���� ���')
    logical_delete = models.BooleanField()
    id_created = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True, db_comment='��� ���� ���� �����')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_inspection'
        db_table_comment = '��� �������'


class AccInspectionHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_date = models.DateTimeField(db_comment='����� �����')
    accident_inspection = models.BigIntegerField(db_comment='����� �������')
    accident_place = models.BigIntegerField(db_comment='��� �����')
    description = models.TextField(blank=True, null=True, db_comment='��� ���� ���� �����')
    from_description = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ���� �������')
    has_media = models.BooleanField(db_comment='��� ���� �� ژ� ���� ���Ͽ')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    operation_at = models.DateTimeField(blank=True, null=True, db_comment='����� ��� ����΍�')
    operation_by = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� ����� ������')
    person_injured_count = models.IntegerField(db_comment='����� ����� ����� ����')
    position = models.BigIntegerField(blank=True, null=True, db_comment='��� ����� ����� ����� ������')
    reporter_other_position = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ��� ����� �����(����)')
    reporter_position = models.BigIntegerField(db_comment='��� ��� ����� �����')
    step = models.CharField(max_length=255, db_comment='���� ���')
    to_description = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ���� �������')
    updated_date = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    to_step = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ����� ���� �������')

    class Meta:
        managed = False
        db_table = 'acc_inspection_history'
        db_table_comment = '������� �������'


class AccInspectionWorkflow(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.BigIntegerField(db_comment='����� �������')
    approve = models.BooleanField(blank=True, null=True, db_comment='����� ����� ���� �����')
    approve_date = models.DateTimeField(blank=True, null=True, db_comment='����� ����� ����� ���� �����')
    cycle = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True, db_comment='�������')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    position = models.IntegerField(db_comment='��� ��� �����: ����� = 0� ���� = 1� ������� ����� = 2')
    referred_profile = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� ���')
    step = models.CharField(max_length=255, db_comment='����� ���� �������')
    step_to = models.CharField(max_length=255, db_comment='����� ���� �������')
    type = models.IntegerField(db_comment='��� ������')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_inspection_workflow'
        db_table_comment = '����� ���'


class AccInspectorReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(AccInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    accident_place = models.BigIntegerField(blank=True, null=True, db_comment='��� �����')
    announcement = models.BigIntegerField(blank=True, null=True, db_comment='����� �������')
    bylaws_description = models.CharField(max_length=4000, blank=True, null=True)
    date_inspection = models.DateTimeField(blank=True, null=True, db_comment='����� ������')
    date_re_inspection = models.DateTimeField(blank=True, null=True, db_comment='����� ������ ����')
    description_not_entery = models.CharField(max_length=4000, blank=True, null=True, db_comment='��� ��� ����� ����')
    has_media = models.BooleanField(blank=True, null=True, db_comment='��� ���� �� ژ� ����� ��ʿ')
    injured_date = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    is_closed_workshop = models.BooleanField(db_comment='��� ��ѐ�� ����� ��ʿ 0=��ѡ 1=���')
    is_elimination_defect = models.BooleanField(blank=True, null=True, db_comment='���� ���� �� ������� 0=��ѡ 1=���')
    is_entrance = models.BooleanField(db_comment='��� ����� ���� �� ��ѐ�� ���� ��� ��ʿ 0=��ѡ 1=���')
    is_letter_judicial_reference = models.BooleanField(blank=True, null=True, db_comment='��� ���� ����� ���� ���Ͽ')
    is_responsibility = models.BooleanField(blank=True, null=True, db_comment='����� ������� ���Ͽ')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=4000, blank=True, null=True, db_comment='�������')
    person_injured_count = models.IntegerField(blank=True, null=True, db_comment='����� ����� ����� ����')
    re_inspection = models.BooleanField(blank=True, null=True, db_comment='���� ������ ����')
    reason_description = models.CharField(max_length=4000, blank=True, null=True, db_comment='��� ���� �����')
    responsibility_description = models.CharField(max_length=4000, blank=True, null=True, db_comment='��� ����� ���� � ������� ��')
    accident_description = models.CharField(max_length=4000, blank=True, null=True, db_comment='��� ���� ���� �����')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    court_referral_reason = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_inspector_report'
        db_table_comment = '��� �����'


class AccOfficialReferrence(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(AccInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    date_letter = models.DateTimeField(db_comment='����� ����')
    letter_number = models.CharField(max_length=255, db_comment='����� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    official_authority = models.BigIntegerField(db_comment='����� ���� ����')
    logical_delete = models.BooleanField(blank=True, null=True)
    modifiedbye = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_official_referrence'
        db_table_comment = '����� ���� �������'


class AccSafetyEquipmentReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(AccInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� �����')
    injured_report = models.ForeignKey(AccInjuredReport, models.DO_NOTHING, db_column='injured_report', db_comment='����� ����� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    safety_equipment = models.BigIntegerField(db_comment='����� ������� �����')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_safety_equipment_report'
        db_table_comment = '������� ����� ���� �� ������ ����� ����'


class AccWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(AccInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    address = models.CharField(max_length=4000, db_comment='����')
    city = models.BigIntegerField(db_comment='����� ������� �� location')
    identity = models.BigIntegerField(blank=True, null=True, db_comment='�� ���')
    latitude = models.FloatField(blank=True, null=True, db_comment='��� ���������')
    longitude = models.FloatField(blank=True, null=True, db_comment='��� ���������')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, db_comment='��� ��ѐ��')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='���� ���� ��ѐ��')
    province = models.BigIntegerField(db_comment='�����')
    zone = models.BigIntegerField(db_comment='����� �������')
    logical_delete = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_workshop'
        db_table_comment = '������ ��ѐ��'


class AccWorkshopActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(AccInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� �����')
    isic_basic_activity = models.BigIntegerField(db_comment='������ ���� ')
    isic_sub_activity = models.BigIntegerField(db_comment='������ ��� ����')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    workshop_shift = models.BigIntegerField(db_comment='���� ���� ��ѐ��')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_workshop_activity'
        db_table_comment = '������ ��ѐ��'


class AccWorkshopReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(AccInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� �����')
    address = models.CharField(max_length=4000, db_comment='����')
    city = models.BigIntegerField(db_comment='������� ��� ��ѐ��')
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, db_comment='��� ��ѐ��')
    national_id = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ��� ��ѐ��')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='���� ���� �� ��� �����')
    postal_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�ρ��� ��ѐ��')
    province = models.BigIntegerField(db_comment='����� ��� ��ѐ��')
    responsible_phone_number = models.CharField(max_length=255, db_comment='���� ����� ��� ����� �� ��ѐ��')
    workers_number = models.IntegerField(db_comment='����� ��ѐ���')
    workshop_code = models.CharField(max_length=255, blank=True, null=True, db_comment='�� ���� ����� ������� ��ѐ��')
    workshop_legal_type = models.BigIntegerField(db_comment='����� ����� ����� ��ѐ��')
    zone = models.BigIntegerField(db_comment='����� ������� ��� ��ѐ��')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_workshop_report'
        db_table_comment = '������ ��� ���� ����� (�����)'


class ActivityDuringAccident(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_during_accident'


class Bank(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_fa = models.CharField(max_length=255, blank=True, null=True)
    iban_identifier = models.CharField(max_length=255, blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'


class BankAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    bank = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    sheba = models.CharField(max_length=255, blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_account'
        unique_together = (('profile', 'sheba'),)


class Basicworkactivity(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basicworkactivity'


class Branchofficer(models.Model):
    id = models.BigAutoField(primary_key=True)
    activefrom = models.DateTimeField(blank=True, null=True)
    activeto = models.DateTimeField(blank=True, null=True)
    branch = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branchofficer'


class CasActivePerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey('CasInspection', models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    active_person = models.IntegerField(db_comment='������� = 0� ������� = 1')
    company_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �ј�')
    first_name = models.CharField(max_length=255, blank=True, null=True, db_comment='���')
    last_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �����ϐ�')
    logical_delete = models.BooleanField()
    national_code = models.CharField(max_length=10, blank=True, null=True, db_comment='����� ���')
    phone = models.CharField(max_length=11, blank=True, null=True, db_comment='����� ����')

    class Meta:
        managed = False
        db_table = 'cas_active_person'
        db_table_comment = '������� ������� � ������� (�������)'


class CasActivePersonReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('CasInspectorReport', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    active_person = models.IntegerField(db_comment='������� = 0� ������� = 1')
    company_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �ј� �������')
    first_name = models.CharField(max_length=255, db_comment='���')
    graduation_level = models.BigIntegerField(blank=True, null=True, db_comment='����� ������� �������')
    last_name = models.CharField(max_length=255, db_comment='��� �����ϐ�')
    national_code = models.CharField(max_length=10, blank=True, null=True, db_comment='����� ���')
    phone = models.CharField(max_length=11, db_comment='����� ����')

    class Meta:
        managed = False
        db_table = 'cas_active_person_report'
        db_table_comment = '������� ������� � ������� (�����)'


class CasAnnouncement(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('CasInspectorReport', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    announcement = models.ForeignKey('InsAnnouncement', models.DO_NOTHING, db_column='announcement', db_comment='����� �����')

    class Meta:
        managed = False
        db_table = 'cas_announcement'
        db_table_comment = '������� ��� ������� �� ��� �����'


class CasArchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey('CasInspection', models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    description = models.CharField(max_length=4000, blank=True, null=True, db_comment='�������')
    letter_number = models.CharField(max_length=20, db_comment='����� ����')

    class Meta:
        managed = False
        db_table = 'cas_archive'
        db_table_comment = '������ ������'


class CasBylawsReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('CasInspectorReport', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    bylaws = models.BigIntegerField(db_comment='����� ���� ���� ���� �� ��� ���')

    class Meta:
        managed = False
        db_table = 'cas_bylaws_report'
        db_table_comment = '���� ���� ��� ��� ���'


class CasDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey('CasInspection', models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    file_type = models.BigIntegerField(db_comment='����� ��� ����')
    logical_delete = models.BooleanField()
    tracking_code = models.CharField(max_length=255, db_comment='����� ���')

    class Meta:
        managed = False
        db_table = 'cas_document'
        db_table_comment = '������� �������'


class CasDocumentReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey('CasInspectorReport', models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    file_type = models.BigIntegerField(db_comment='����� ��� ����')
    tracking_code = models.CharField(max_length=255, db_comment='����� ���')

    class Meta:
        managed = False
        db_table = 'cas_document_report'
        db_table_comment = '������� �����'


class CasInspection(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    logical_delete = models.BooleanField()
    status = models.CharField(max_length=255, db_comment='����� �������')

    class Meta:
        managed = False
        db_table = 'cas_inspection'
        db_table_comment = '��� �������'


class CasInspectionHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    accident_inspection = models.ForeignKey(CasInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    logical_delete = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    operation_at = models.DateTimeField(blank=True, null=True, db_comment='����� ��� ����΍�')
    operation_by = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� ����� ������')
    position = models.ForeignKey('Position', models.DO_NOTHING, db_column='position', blank=True, null=True, db_comment='��� ����� ����� ����� ������')
    status = models.CharField(max_length=255, db_comment='����� �������')
    status_description = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ���� �������')
    to_status = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ����� ���� �������')
    to_status_description = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ���� �������')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cas_inspection_history'
        db_table_comment = '������� �������'


class CasInspectionWorkflow(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(CasInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    approve = models.BooleanField(blank=True, null=True, db_comment='����� ����� ���� �����')
    approve_date = models.DateTimeField(blank=True, null=True, db_comment='����� ����� ����� ���� �����')
    description = models.CharField(max_length=4000, blank=True, null=True, db_comment='�������')
    position = models.ForeignKey('Position', models.DO_NOTHING, db_column='position', db_comment='��� ��� �����: ����� = 0� ���� = 1� ������� ����� = 2')
    referred_profile = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� ���')
    step = models.CharField(max_length=255, db_comment='����� ���� �������')
    step_to = models.CharField(max_length=255, db_comment='����� ���� �������')
    type = models.IntegerField(db_comment='��� ������')

    class Meta:
        managed = False
        db_table = 'cas_inspection_workflow'
        db_table_comment = '����� ���'


class CasInspectorReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(CasInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    date_inspection = models.DateTimeField(blank=True, null=True, db_comment='����� ������')
    date_re_inspection = models.DateTimeField(blank=True, null=True, db_comment='����� ����� ����')
    description_not_entery = models.CharField(max_length=4000, blank=True, null=True, db_comment='��� ��� ����� ����')
    is_announcement = models.BooleanField(blank=True, null=True, db_comment='���� ���� �� �������')
    is_article154 = models.BooleanField(blank=True, null=True, db_comment='���� ����� ���� 154')
    is_closed_workshop = models.BooleanField(blank=True, null=True, db_comment='���� ������ ��ѐ��')
    is_entrance = models.BooleanField(blank=True, null=True, db_comment='���� ����� ���� �� ��ѐ��')
    is_re_inspection = models.BooleanField(blank=True, null=True, db_comment='���� ���� �� ������ ����')
    is_view_workshop_history = models.BooleanField(db_comment='���� ������ ����� ��ѐ��')
    note = models.CharField(max_length=4000, blank=True, null=True, db_comment='�������')
    report_description = models.TextField(blank=True, null=True, db_comment='��� ����� ������ �����')

    class Meta:
        managed = False
        db_table = 'cas_inspector_report'
        db_table_comment = '��� �����'


class CasInspectorWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(CasInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    address = models.CharField(max_length=4000, db_comment='����� ���� ��ѐ��')
    city = models.ForeignKey('Location', models.DO_NOTHING, db_column='city', db_comment='�������')
    fax = models.CharField(max_length=11, blank=True, null=True, db_comment='������ ��ѐ��')
    name = models.CharField(max_length=50, db_comment='��� ��ѐ��')
    national_id = models.CharField(max_length=11, blank=True, null=True, db_comment='����� ��� ��ѐ��')
    phone = models.CharField(max_length=11, blank=True, null=True, db_comment='���� ���� ��ѐ��')
    postal_code = models.CharField(max_length=10, blank=True, null=True, db_comment='�ρ��� ��ѐ��')
    province = models.ForeignKey('Location', models.DO_NOTHING, db_column='province', related_name='casinspectorworkshop_province_set', db_comment='�����')
    workshop_code = models.CharField(max_length=10, blank=True, null=True, db_comment='�� ����� ������� ��ѐ��')
    workshop_legal_type = models.ForeignKey('WorkshopLegalType', models.DO_NOTHING, db_column='workshop_legal_type', db_comment='����� ����� ����� ��ѐ��')
    workshop_status = models.ForeignKey('WorkshopStatus', models.DO_NOTHING, db_column='workshop_status', db_comment='����� ����� ��ѐ��')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', db_comment='����� �������')

    class Meta:
        managed = False
        db_table = 'cas_inspector_workshop'
        db_table_comment = '������� ��ѐ��(�����)'


class CasItemsToCheckedRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(CasInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    items_to_checked = models.ForeignKey('InsItemsToChecked', models.DO_NOTHING, db_column='items_to_checked', db_comment='���� ������� ����� �� ��ϐ�� ����� �����')
    logical_delete = models.BooleanField()
    workshop = models.ForeignKey('CasWorkshop', models.DO_NOTHING, db_column='workshop', db_comment='����� ������ ��ѐ��')

    class Meta:
        managed = False
        db_table = 'cas_items_to_checked_request'
        db_table_comment = '����� ������� ����� �� ��ϐ�� ����� �����'


class CasOfficialReferrence(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(CasInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    date_letter = models.DateTimeField(db_comment='����� ����')
    letter_number = models.CharField(max_length=20, db_comment='����� ����')
    logical_delete = models.BooleanField()
    official_authority = models.BigIntegerField(db_comment='���� ����')

    class Meta:
        managed = False
        db_table = 'cas_official_referrence'
        db_table_comment = '����� ���� (�������)'


class CasReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(CasInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    report = models.BigIntegerField(db_comment='����� �����')

    class Meta:
        managed = False
        db_table = 'cas_report'
        db_table_comment = '����� ��� ������� �� ��� �����'


class CasStateOfAmenities(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(CasInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    amenity = models.BigIntegerField(db_comment='����� ����� ������ �����')
    other = models.CharField(max_length=4000, blank=True, null=True, db_comment='����')

    class Meta:
        managed = False
        db_table = 'cas_state_of_amenities'
        db_table_comment = '����� ������ ����� (�����)'


class CasWorkerStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(CasInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    address_central_office = models.CharField(max_length=4000, blank=True, null=True, db_comment='���� ���� �ј��')
    area = models.BigIntegerField(blank=True, null=True, db_comment='����� ���� ��ѐ�� (�������)')
    ceo_first_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� ��������')
    ceo_last_name = models.CharField(max_length=255, blank=True, null=True, db_comment='��� �����ϐ� ��������')
    infrastructure = models.BigIntegerField(blank=True, null=True, db_comment='��� ��� ��� (�������)')
    is_activity_license = models.BooleanField(blank=True, null=True, db_comment='������ ������/ ������ ���� ������')
    is_civil_lability_insurance = models.BooleanField(blank=True, null=True, db_comment='���� ������� ����')
    is_compliance_minimum_wage = models.BooleanField(blank=True, null=True, db_comment='����� ������')
    is_confirmation_article87 = models.BooleanField(blank=True, null=True, db_comment='������� ���� 87')
    is_establishment_permit = models.BooleanField(blank=True, null=True, db_comment='���� �����')
    is_protection_tchnical_committee = models.BooleanField(blank=True, null=True, db_comment='����� ��� ����� � ������')
    is_responsible_technical_protection = models.BooleanField(blank=True, null=True, db_comment='����� ����� ���')
    isforced_labor = models.BooleanField(blank=True, null=True, db_comment='��� ������')
    ishard_ad_hrmful = models.BooleanField(blank=True, null=True, db_comment='����� ��� � ���� ���')
    job_classification_scheme = models.ForeignKey('InsJobClassification', models.DO_NOTHING, db_column='job_classification_scheme', db_comment='����� ��� ���� ���� �����')
    labor_organizations = models.ForeignKey('InsLabor', models.DO_NOTHING, db_column='labor_organizations', blank=True, null=True, db_comment='����� �Ԙ� ��� ��ѐ��')
    number_all_workers = models.IntegerField(db_comment='����� �� ��ѐ���')
    number_employed_people_under15 = models.IntegerField(blank=True, null=True, db_comment='����� ����� ���� ��� 15 ���')
    number_female_workers = models.IntegerField(blank=True, null=True, db_comment='����� ��ѐ��� ��')
    number_intern = models.IntegerField(blank=True, null=True, db_comment='����� ���������')
    number_licensed_foreign_workers = models.IntegerField(blank=True, null=True, db_comment='����� ��ѐ��� ����� ������ ���')
    number_male_workers = models.IntegerField(blank=True, null=True, db_comment='����� ��ѐ��� ���')
    number_no_licensed_foreign_workers = models.IntegerField(blank=True, null=True, db_comment='����� ��ѐ��� ����� ���� ������')
    number_workers_between15 = models.IntegerField(blank=True, null=True, db_comment='����� ��ѐ��� ������ 15 �� 18 ���')
    phone_central_office = models.CharField(max_length=11, blank=True, null=True, db_comment='���� ���� �ј��')
    re_inspection_priority = models.BigIntegerField(db_comment='����� ������ ������ ����')

    class Meta:
        managed = False
        db_table = 'cas_worker_status'
        db_table_comment = '������� ����� ��ѐ��� (�����)'


class CasWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspection = models.ForeignKey(CasInspection, models.DO_NOTHING, db_column='accident_inspection', db_comment='����� �������')
    address = models.CharField(max_length=4000, db_comment='����� ���� ��ѐ��')
    city = models.ForeignKey('Location', models.DO_NOTHING, db_column='city', db_comment='�������')
    identity = models.BigIntegerField(blank=True, null=True, db_comment='����� ���')
    latitude = models.FloatField(blank=True, null=True, db_comment='��� ���������')
    logical_delete = models.BooleanField()
    longitude = models.FloatField(blank=True, null=True, db_comment='��� ���������')
    name = models.CharField(max_length=50, db_comment='��� ��ѐ��')
    other_item = models.CharField(max_length=4000, blank=True, null=True, db_comment='���� ������� �����')
    phone = models.CharField(max_length=11, blank=True, null=True, db_comment='���� ���� ��ѐ��')
    postal_code = models.CharField(max_length=10, blank=True, null=True, db_comment='�ρ��� ��ѐ��')
    province = models.ForeignKey('Location', models.DO_NOTHING, db_column='province', related_name='casworkshop_province_set', db_comment='�����')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', db_comment='����� �������')

    class Meta:
        managed = False
        db_table = 'cas_workshop'
        db_table_comment = '������ ��ѐ�� (�������)'


class CasWorkshopActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby', blank=True, null=True, db_comment='����� ����� ����� �����')
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True, db_comment='����� �����')
    modifiedby = models.BigIntegerField(blank=True, null=True, db_comment='����� ����� ����� �����')
    version = models.BigIntegerField()
    accident_inspector_report = models.ForeignKey(CasInspectorReport, models.DO_NOTHING, db_column='accident_inspector_report', db_comment='����� ����� ������')
    isic_basic_activity = models.ForeignKey('IsicActivity', models.DO_NOTHING, db_column='isic_basic_activity', db_comment='������ ��ѐ��')
    isic_basic_activity_friday = models.ForeignKey('InsWorkshopActivityFriday', models.DO_NOTHING, db_column='isic_basic_activity_friday', db_comment='����� ������ ��ѐ�� �� ������ ����')
    isic_sub_activity = models.ForeignKey('IsicActivity', models.DO_NOTHING, db_column='isic_sub_activity', related_name='casworkshopactivity_isic_sub_activity_set', db_comment='����� ������ ��ѐ�� (��� ����)')
    number_shift_work = models.ForeignKey('InsNumberWorkShifts', models.DO_NOTHING, db_column='number_shift_work', blank=True, null=True, db_comment='����� ����� ���� ����')
    product = models.CharField(max_length=255, db_comment='�� ����� ������ (����)')
    shift_work = models.ForeignKey('WorkShift', models.DO_NOTHING, db_column='shift_work', db_comment='����� ���� ����')
    sub_product = models.ForeignKey('Product', models.DO_NOTHING, db_column='sub_product', db_comment='����� ����� ������ (��ѐ���)')
    turn_work = models.ForeignKey('InsTimeWork', models.DO_NOTHING, db_column='turn_work', db_comment='����� ���� ����')

    class Meta:
        managed = False
        db_table = 'cas_workshop_activity'
        db_table_comment = '������� ������ ��ѐ�� (�����)'


class CipostType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cipost_type'


class ComAppealrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    appealrequester = models.BigIntegerField()
    indictment = models.BigIntegerField()
    titlereason = models.CharField(max_length=255, blank=True, null=True)
    reasondescription = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    requestertypecode = models.BigIntegerField(blank=True, null=True)
    requestertypedescription = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_appealrequest'


class ComAppealrequestdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    apealrequest = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_appealrequestdocument'


class ComCancelrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    cancelrequester = models.BigIntegerField()
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    description = models.CharField(max_length=255)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_cancelrequest'


class ComCancelrequestdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    cancelrequest = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_cancelrequestdocument'


class ComComplainanttype(models.Model):
    createdat = models.DateTimeField()
    createdby = models.FloatField()
    #id = models.FloatField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'com_complainanttype'


class ComComplaining(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=1000)
    companyname = models.CharField(max_length=50, blank=True, null=True)
    complainingtype = models.BigIntegerField()
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    faxnumber = models.CharField(max_length=20, blank=True, null=True)
    fidacode = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    highestresponsiblefirstname = models.CharField(max_length=50, blank=True, null=True)
    highestresponsiblelastname = models.CharField(max_length=50, blank=True, null=True)
    highestresponsiblenationalcode = models.CharField(max_length=50, blank=True, null=True)
    highestresponsibletype = models.BigIntegerField(blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    location = models.BigIntegerField()
    mobilenumber = models.CharField(max_length=20, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    nationalcode = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.BigIntegerField(blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    zone = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_complaining'


class ComComplaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    canceled = models.BooleanField(blank=True, null=True)
    complainanttype = models.BigIntegerField(blank=True, null=True)
    complainingtype = models.BigIntegerField(blank=True, null=True)
    contracttype = models.BigIntegerField(blank=True, null=True)
    filledbycomplainant = models.BooleanField(blank=True, null=True)
    finalsalary = models.BigIntegerField(blank=True, null=True)
    firstviewedat = models.DateTimeField(blank=True, null=True)
    firstviewedby = models.BigIntegerField(blank=True, null=True)
    hasinsurance = models.BooleanField(blank=True, null=True)
    jobtitle = models.CharField(max_length=200, blank=True, null=True)
    paymentmethod = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    requestcode = models.BigIntegerField(blank=True, null=True)
    requestdescription = models.CharField(max_length=4000, blank=True, null=True)
    requesttitle = models.CharField(max_length=255, blank=True, null=True)
    salary = models.BigIntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    step = models.CharField(max_length=255, blank=True, null=True)
    tamininsurancenumber = models.CharField(max_length=20, blank=True, null=True)
    taminworkshopcode = models.BigIntegerField(blank=True, null=True)
    totalexperiencesday = models.BigIntegerField(blank=True, null=True)
    totalexperiencesmonth = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    workshopaddress = models.CharField(max_length=255, blank=True, null=True)
    workshopcertificateid = models.CharField(max_length=20, blank=True, null=True)
    workshopemail = models.CharField(max_length=100, blank=True, null=True)
    workshopexperiencesday = models.CharField(max_length=255, blank=True, null=True)
    workshopexperiencesmonth = models.BigIntegerField(blank=True, null=True)
    workshopfax = models.CharField(max_length=20, blank=True, null=True)
    workshopguildnumber = models.CharField(max_length=20, blank=True, null=True)
    workshoplegalid = models.CharField(max_length=11, blank=True, null=True)
    workshoplocation = models.BigIntegerField(blank=True, null=True)
    workshopmobile = models.CharField(max_length=20, blank=True, null=True)
    workshopname = models.CharField(max_length=100, blank=True, null=True)
    workshopphone = models.CharField(max_length=20, blank=True, null=True)
    workshoppostalcode = models.CharField(max_length=10, blank=True, null=True)
    workshopzone = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_complaint'


class ComComplaintHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    historyid = models.BigIntegerField()
    complainanttype = models.BigIntegerField(blank=True, null=True)
    contracttype = models.BigIntegerField(blank=True, null=True)
    filledbycomplainant = models.BooleanField(blank=True, null=True)
    finalsalary = models.BigIntegerField(blank=True, null=True)
    firstviewedat = models.DateTimeField(blank=True, null=True)
    firstviewedby = models.BigIntegerField(blank=True, null=True)
    fromdescription = models.CharField(max_length=255, blank=True, null=True)
    fromstate = models.CharField(max_length=255, blank=True, null=True)
    fromstep = models.CharField(max_length=255, blank=True, null=True)
    hasinsurance = models.BooleanField(blank=True, null=True)
    jobtitle = models.CharField(max_length=200, blank=True, null=True)
    operation_at = models.DateTimeField(blank=True, null=True)
    operation_by = models.BigIntegerField(blank=True, null=True)
    paymentmethod = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    requestcode = models.BigIntegerField(blank=True, null=True)
    requestdescription = models.CharField(max_length=255, blank=True, null=True)
    requesttitle = models.CharField(max_length=255, blank=True, null=True)
    salary = models.BigIntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    step = models.CharField(max_length=255, blank=True, null=True)
    taminworkshopcode = models.BigIntegerField(blank=True, null=True)
    todescription = models.CharField(max_length=255, blank=True, null=True)
    totalexperiencesday = models.BigIntegerField(blank=True, null=True)
    totalexperiencesmonth = models.BigIntegerField(blank=True, null=True)
    workshopaddress = models.CharField(max_length=255, blank=True, null=True)
    workshopemail = models.CharField(max_length=100, blank=True, null=True)
    workshopexperiencesday = models.CharField(max_length=255, blank=True, null=True)
    workshopexperiencesmonth = models.BigIntegerField(blank=True, null=True)
    workshopfax = models.CharField(max_length=20, blank=True, null=True)
    workshopguildnumber = models.CharField(max_length=20, blank=True, null=True)
    workshoplocation = models.BigIntegerField(blank=True, null=True)
    workshopmobile = models.CharField(max_length=20, blank=True, null=True)
    workshopname = models.CharField(max_length=100, blank=True, null=True)
    workshopphone = models.CharField(max_length=20, blank=True, null=True)
    workshoppostalcode = models.CharField(max_length=10, blank=True, null=True)
    workshopzone = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_complaint_history'


class ComComplaintdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    uploadertype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_complaintdocument'


class ComComplaintrequestsubject(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    meeting = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    requestsubject = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_complaintrequestsubject'


class ComCompromise(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.BigIntegerField()
    document = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.BigIntegerField(blank=True, null=True)
    enabled = models.BooleanField()
    profile = models.BigIntegerField()
    isactive = models.BooleanField()
    version = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_compromise'


class ComDeceased(models.Model):
    id = models.BigAutoField(primary_key=True)
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    nationalcode = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'com_deceased'


class ComDeceaseddocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    deceased = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_deceaseddocument'


class ComIndictment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    code = models.CharField(max_length=20)
    complainant = models.BigIntegerField(blank=True, null=True)
    complaining = models.BigIntegerField(blank=True, null=True)
    confirmationdate = models.DateTimeField(blank=True, null=True)
    confirmedby = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    deliveryreceipt = models.CharField(max_length=255, blank=True, null=True)
    deliverytype = models.BigIntegerField(blank=True, null=True)
    electronicsend = models.BooleanField()
    filetemplate = models.BigIntegerField(blank=True, null=True)
    meeting = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    sendinvitationdate = models.DateTimeField(blank=True, null=True)
    indictmentcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'com_indictment'


class ComInvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    complaining = models.BigIntegerField(blank=True, null=True)
    confirmationdate = models.DateTimeField(blank=True, null=True)
    confirmedby = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    deliveryreceipt = models.CharField(max_length=255, blank=True, null=True)
    deliverytype = models.BigIntegerField(blank=True, null=True)
    electronicsend = models.BooleanField()
    filetemplate = models.BigIntegerField(blank=True, null=True)
    meeting = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    sendinvitationdate = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_invitation'


class ComInvitationHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    invitation_id = models.BigIntegerField()
    operation_at = models.DateTimeField()
    operation_by = models.BigIntegerField()
    profile = models.BigIntegerField()
    type = models.IntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_invitation_history'


class ComJudgment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    judgmentamount = models.BigIntegerField(blank=True, null=True)
    judgmenttext = models.TextField()
    judgmenttype = models.BigIntegerField()
    meeting = models.BigIntegerField()
    minutesdocument = models.CharField(max_length=255)
    minutesummery = models.TextField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    referdescription = models.CharField(max_length=4000, blank=True, null=True)
    savetype = models.IntegerField()
    version = models.BigIntegerField()
    increasecycle = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_judgment'


class ComJudgmentsubject(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.BigIntegerField()
    createdate = models.DateTimeField()
    createdby = models.BigIntegerField()
    judgment = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_judgmentsubject'


class ComJudgmenttype(models.Model):
    createdat = models.DateTimeField()
    createdby = models.FloatField()
    #id = models.FloatField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    parentid = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    workflowstate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'com_judgmenttype'


class ComMeeting(models.Model):
    id = models.BigAutoField(primary_key=True)
    committee = models.BigIntegerField()
    committeebranch = models.BigIntegerField()
    committeebranchchangereason = models.CharField(max_length=255, blank=True, null=True)
    committeecalendar = models.BigIntegerField()
    committeecalendarinused = models.BigIntegerField()
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    meetingdatetime = models.DateTimeField()
    meetingnumber = models.BigIntegerField()
    membersfills = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    setcalendarmanualreason = models.CharField(max_length=255, blank=True, null=True)
    setcalendarmanualtype = models.BigIntegerField(blank=True, null=True)
    setcalendartype = models.IntegerField()
    workflowstate = models.CharField(max_length=255)
    cycle = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_meeting'


class ComRepresentative(models.Model):
    id = models.BigAutoField(primary_key=True)
    appealright = models.BooleanField()
    appointedby = models.BigIntegerField()
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    executionright = models.BooleanField()
    isactive = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    representativeprofile = models.BigIntegerField()
    representativetype = models.BigIntegerField()
    version = models.BigIntegerField()
    status = models.IntegerField(blank=True, null=True)
    resigndate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_representative'


class ComRepresentativedocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    representative = models.BigIntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_representativedocument'


class ComSetcalendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    calendarmanualtype = models.BigIntegerField(blank=True, null=True)
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    meeting = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    rejecttype = models.BigIntegerField(blank=True, null=True)
    setcalendartype = models.BigIntegerField()
    txtfaultaddressreason = models.CharField(max_length=255, blank=True, null=True)
    wrongrequestreason = models.CharField(max_length=255, blank=True, null=True)
    is_rejected = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_setcalendar'


class ComSetcalendarmanualtype(models.Model):
    code = models.FloatField()
    createdate = models.DateTimeField(blank=True, null=True)
    createdby = models.FloatField()
    #id = models.FloatField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    name = models.FloatField()
    createdat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'com_setcalendarmanualtype'


class ComSetcalendartype(models.Model):
    code = models.BigIntegerField()
    createdby = models.FloatField()
    #id = models.FloatField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    name = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_setcalendartype'


class ComSpeciallistreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    assigndate = models.DateTimeField()
    assignedby = models.BigIntegerField()
    assignedto = models.BigIntegerField()
    confidentialityreason = models.CharField(max_length=255, blank=True, null=True)
    confirmedby = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    isconfidentiality = models.BooleanField(blank=True, null=True)
    meeting = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    reportissuedate = models.DateTimeField(blank=True, null=True)
    reportsducument = models.CharField(max_length=255, blank=True, null=True)
    specialtype = models.BigIntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_speciallistreport'


class ComSubject(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50)
    subjecttype = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_subject'


class ComSubjectiondocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    abandoned = models.BooleanField(blank=True, null=True)
    courtjudgmentdocument = models.CharField(max_length=255, blank=True, null=True)
    courtjudgmentdocumentsubmitdate = models.DateTimeField(blank=True, null=True)
    courtregistrationdocument = models.CharField(max_length=255, blank=True, null=True)
    courtregistrationdocumentsubmitdate = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    meeting = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_subjectiondocument'


class ComTaminbranchofficerreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    tamininvitation = models.BigIntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_taminbranchofficerreport'


class ComTamininvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    assigndate = models.DateTimeField(blank=True, null=True)
    branch = models.BigIntegerField(blank=True, null=True)
    branchdescription = models.CharField(max_length=255, blank=True, null=True)
    branchofficer = models.BigIntegerField(blank=True, null=True)
    chiefofficer = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    meeting = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_tamininvitation'


class ComTrialcommitteemember(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeearangement = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    hasdone = models.BooleanField(blank=True, null=True)
    meeting = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    rolecall = models.BooleanField(blank=True, null=True)
    committeearrangement = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_trialcommitteemember'


class ComTrialexecution(models.Model):
    id = models.BigAutoField(primary_key=True)
    complaint = models.BigIntegerField()
    confirmedat = models.DateTimeField(blank=True, null=True)
    confirmedby = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    executionrequestedat = models.DateTimeField()
    executionrequestedby = models.BigIntegerField()
    executiontext = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    executionrequestercode = models.BigIntegerField(blank=True, null=True)
    executionrequestertype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_trialexecution'


class ComTrialvote(models.Model):
    id = models.BigAutoField(primary_key=True)
    agreement = models.BooleanField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    judgment = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    trialcommitteemember = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_trialvote'


class ComUnderguardianship(models.Model):
    id = models.BigAutoField(primary_key=True)
    complaint = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    nationalcode = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'com_underguardianship'


class ComUnderguardianshipdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    underguardianship = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'com_underguardianshipdocument'


class Committee(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='آدرس')
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name='کد کمیته')
    commiteetype = models.BigIntegerField(blank=True, null=True, verbose_name='نوع کمیته')
    createdat = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ ایجاد')
    createdby = models.BigIntegerField(blank=True, null=True, verbose_name='ایجاد شده توسط')
    isactive = models.BooleanField(blank=True, null=True, verbose_name='وضعیت')
    modifiedat = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ بروزرسانی')
    modifiedby = models.BigIntegerField(blank=True, null=True, verbose_name='بروزرسانی شده توسط')
    name = models.CharField(max_length=70, blank=True, null=True, verbose_name='نام کمیته')
    office = models.ForeignKey('office', models.DO_NOTHING, db_column='office', blank=True, null=True, verbose_name='اداره')
    version = models.BigIntegerField(blank=True, null=True, verbose_name='نسخه')

    class Meta:
        managed = False
        db_table = 'committee'
        verbose_name = 'کمیته'
        verbose_name_plural = 'کمیته ها'

    def __str__(self):
        #office_name = self.office.name if self.office else 'No Office'
        return self.name


class CommitteeTimeDuration(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committee_time_duration'


class Committeearrangement(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeetype = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    membercount = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    role = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committeearrangement'


class Committeebranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    committee = models.ForeignKey('Committee', models.DO_NOTHING, db_column='committee', blank=True, null=True, verbose_name='کمیته')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.FloatField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committeebranch'

    def __str__(self):
        return self.name


class Committeecalendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    availabledate = models.DateTimeField(verbose_name='تاریخ های دردسترس')
    availabletrialcount = models.BigIntegerField(verbose_name='تعداد جلسات دردسترس')
    committee = models.ForeignKey(Committee, models.DO_NOTHING, db_column='committee', verbose_name='کمیته')
    createdat = models.DateTimeField(verbose_name='تاریخ ایجاد')
    createdby = models.BigIntegerField(verbose_name='ایجاد شده توسط')
    maxdurationofeachmeeting = models.IntegerField(verbose_name='زمان هر جلسه')
    modifiedat = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ بروزرسانی')
    modifiedby = models.BigIntegerField(blank=True, null=True, verbose_name='بروزرسانی شده توسط')
    trialcount = models.BigIntegerField(verbose_name='تعداد جلسات')
    version = models.BigIntegerField(verbose_name='نسخه')
    branch = models.ForeignKey(Committeebranch, models.DO_NOTHING, db_column='branch', verbose_name='شعبه')
    isactive = models.BooleanField(blank=True, null=True, verbose_name='وضعیت')

    class Meta:
        managed = False
        db_table = 'committeecalendar'
        verbose_name = 'تقویم کمیته '
        verbose_name_plural = 'تقویم کمیته ها'

    def __str__(self):
        return str(self.committee)


class Committeecalendarinused(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeecalendar = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    requestcode = models.BigIntegerField(blank=True, null=True)
    usedmeetingdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committeecalendarinused'


class Committeesupportlocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    committee = models.ForeignKey(Committee, models.DO_NOTHING, verbose_name='کمیته', db_column='committee')
    location = models.BigIntegerField(blank=True, null=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, verbose_name='محله شهرداری', db_column='zone')
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committeesupportlocation'
        verbose_name = 'موقعیت مکانی کمیته'
        verbose_name_plural = 'موقعیت مکانی کمیته ها'

    def __str__(self):
        return str(self.committee)


class Committeetype(models.Model):
    #id = models.FloatField()
    code = models.CharField(max_length=20, blank=True, null=True)
    createdat = models.DateField(blank=True, null=True)
    createdby = models.FloatField(blank=True, null=True)
    isactive = models.FloatField(blank=True, null=True)
    modifiedat = models.DateField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    ishqoffice = models.FloatField(blank=True, null=True)
    parentid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committeetype'


class Committeeworkflowstate(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeetype = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    workflowstste = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committeeworkflowstate'


class CompanyPerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_datesh = models.CharField(max_length=255, blank=True, null=True)
    capital_status = models.CharField(max_length=255, blank=True, null=True)
    clearance_confession_status = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    first_namefa = models.CharField(max_length=255, blank=True, null=True)
    last_namefa = models.CharField(max_length=255, blank=True, null=True)
    managing_confession_status = models.CharField(max_length=255, blank=True, null=True)
    mobile_number4sms = models.CharField(max_length=255, blank=True, null=True)
    nationality_code = models.CharField(max_length=255, blank=True, null=True)
    person_number = models.CharField(max_length=255, blank=True, null=True)
    person_type = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    sso_legal_account_info = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_person'


class CompanyPersonPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_non_direct_member = models.CharField(max_length=255, blank=True, null=True)
    is_non_partnership = models.CharField(max_length=255, blank=True, null=True)
    managing_confession_status = models.CharField(max_length=255, blank=True, null=True)
    period_time = models.CharField(max_length=255, blank=True, null=True)
    signature_state = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    company_person = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_person_post'


class Complaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    canceled = models.BooleanField(blank=True, null=True)
    complainanttype = models.BigIntegerField(blank=True, null=True)
    complainingtype = models.BigIntegerField(blank=True, null=True)
    contracttype = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    filledbycomplainant = models.BooleanField(blank=True, null=True)
    finalsalary = models.BigIntegerField(blank=True, null=True)
    firstviewedat = models.DateTimeField(blank=True, null=True)
    firstviewedby = models.BigIntegerField(blank=True, null=True)
    hasinsurance = models.BooleanField(blank=True, null=True)
    jobtitle = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    paymentmethod = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    requestcode = models.BigIntegerField(blank=True, null=True)
    requestdescription = models.CharField(max_length=4000, blank=True, null=True)
    requesttitle = models.CharField(max_length=255, blank=True, null=True)
    salary = models.BigIntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    step = models.CharField(max_length=255, blank=True, null=True)
    tamininsurancenumber = models.CharField(max_length=255, blank=True, null=True)
    taminworkshopcode = models.BigIntegerField(blank=True, null=True)
    totalexperiencesday = models.BigIntegerField(blank=True, null=True)
    totalexperiencesmonth = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    workshopaddress = models.CharField(max_length=255, blank=True, null=True)
    workshopcertificateid = models.CharField(max_length=255, blank=True, null=True)
    workshopemail = models.CharField(max_length=255, blank=True, null=True)
    workshopexperiencesday = models.CharField(max_length=255, blank=True, null=True)
    workshopexperiencesmonth = models.BigIntegerField(blank=True, null=True)
    workshopfax = models.CharField(max_length=255, blank=True, null=True)
    workshopguildnumber = models.CharField(max_length=255, blank=True, null=True)
    workshoplegalid = models.CharField(max_length=255, blank=True, null=True)
    workshoplocation = models.BigIntegerField(blank=True, null=True)
    workshopmobile = models.CharField(max_length=255, blank=True, null=True)
    workshopname = models.CharField(max_length=255, blank=True, null=True)
    workshopphone = models.CharField(max_length=255, blank=True, null=True)
    workshoppostalcode = models.CharField(max_length=255, blank=True, null=True)
    workshopzone = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint'


class Configs(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    config_name = models.CharField(max_length=255, blank=True, null=True)
    config_value = models.CharField(max_length=255, blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configs'


class ContContract(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.BigIntegerField(blank=True, null=True)
    childallowance = models.BigIntegerField(blank=True, null=True)
    contractenddate = models.DateTimeField(blank=True, null=True)
    contractfile = models.CharField(max_length=255, blank=True, null=True)
    contractstartdate = models.DateTimeField(blank=True, null=True)
    contracttype = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    employee = models.BigIntegerField(blank=True, null=True)
    employeeiban = models.CharField(max_length=255, blank=True, null=True)
    employeenationalid = models.CharField(max_length=255, blank=True, null=True)
    employeerevisionrequestreason = models.CharField(max_length=255, blank=True, null=True)
    employer = models.BigIntegerField(blank=True, null=True)
    employercontractrejectionreason = models.CharField(max_length=255, blank=True, null=True)
    employertype = models.BigIntegerField(blank=True, null=True)
    fixedsalary = models.BigIntegerField(blank=True, null=True)
    housingallowance = models.BigIntegerField(blank=True, null=True)
    jobtitle = models.CharField(max_length=255, blank=True, null=True)
    jobtitletype = models.BigIntegerField(blank=True, null=True)
    laborcoupon = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    monthsalary = models.BigIntegerField(blank=True, null=True)
    registerdatebyemployer = models.DateTimeField(blank=True, null=True)
    step = models.CharField(max_length=255, blank=True, null=True)
    workendtime = models.DateTimeField(blank=True, null=True)
    workskilllevel = models.BigIntegerField(blank=True, null=True)
    workshopaddress = models.CharField(max_length=255, blank=True, null=True)
    workshoplegalid = models.CharField(max_length=255, blank=True, null=True)
    workshopname = models.CharField(max_length=255, blank=True, null=True)
    workshoppostalcode = models.CharField(max_length=255, blank=True, null=True)
    workstarttime = models.DateTimeField(blank=True, null=True)
    zone = models.BigIntegerField(blank=True, null=True)
    employercontractrjectiondate = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    yearsofserviceallowance = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cont_contract'


class ContContractRevocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_id = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    revocation_date = models.DateTimeField()
    revocation_reason = models.CharField(max_length=255)
    revoker_profile_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cont_contract_revocation'
# Unable to inspect table 'cont_contract_revocation_document'
# The error was: ORA-00942: table or view does not exist



class ContContractdocumnet(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cont_contractdocumnet'


class ContContracthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isaccepted = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    step = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_contracthistory'


class Contracttype(models.Model):
    isexpireable = models.FloatField(blank=True, null=True)
    createdat = models.DateField(blank=True, null=True)
    createdby = models.FloatField(blank=True, null=True)
    #id = models.FloatField()
    modifiedat = models.DateField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracttype'


class CourtReferralReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    desciption = models.CharField(max_length=255, blank=True, null=True)
    en_key = models.CharField(max_length=255, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'court_referral_reason'


class Deliverytype(models.Model):
    isactive = models.FloatField(blank=True, null=True)
    #id = models.FloatField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliverytype'


class DjangoAdminInterface(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    active = models.BooleanField()
    title = models.CharField(max_length=50, blank=True, null=True)
    title_visible = models.BooleanField()
    logo = models.CharField(max_length=100, blank=True, null=True)
    logo_visible = models.BooleanField()
    css_header_background_color = models.CharField(max_length=10, blank=True, null=True)
    title_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_background_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_rounded_corners = models.BooleanField()
    css_generic_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_generic_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_background99e4 = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_background20f4 = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_backgroue0b7 = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_backgroua080 = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_text_color = models.CharField(max_length=10, blank=True, null=True)
    list_filter_dropdown = models.BooleanField()
    related_modal_active = models.BooleanField()
    related_modal_background_color = models.CharField(max_length=10, blank=True, null=True)
    related_modal_rounded_corners = models.BooleanField()
    logo_color = models.CharField(max_length=10, blank=True, null=True)
    recent_actions_visible = models.BooleanField()
    favicon = models.CharField(max_length=100, blank=True, null=True)
    related_modal_background_oe111 = models.CharField(max_length=5, blank=True, null=True)
    env_name = models.CharField(max_length=50, blank=True, null=True)
    env_visible_in_header = models.BooleanField()
    env_color = models.CharField(max_length=10, blank=True, null=True)
    env_visible_in_favicon = models.BooleanField()
    related_modal_close_button3b73 = models.BooleanField()
    language_chooser_active = models.BooleanField()
    language_chooser_display = models.CharField(max_length=10, blank=True, null=True)
    list_filter_sticky = models.BooleanField()
    form_pagination_sticky = models.BooleanField()
    form_submit_sticky = models.BooleanField()
    css_module_background_sele1a15 = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_selected_color = models.CharField(max_length=10, blank=True, null=True)
    logo_max_height = models.IntegerField()
    logo_max_width = models.IntegerField()
    foldable_apps = models.BooleanField()
    language_chooser_control = models.CharField(max_length=20, blank=True, null=True)
    list_filter_highlight = models.BooleanField()
    list_filter_removal_links = models.BooleanField()
    show_fieldsets_as_tabs = models.BooleanField()
    show_inlines_as_tabs = models.BooleanField()
    css_generic_link_active_color = models.CharField(max_length=10, blank=True, null=True)
    collapsible_stacked_inlines = models.BooleanField()
    collapsible_stacked_inlineed3b = models.BooleanField()
    collapsible_tabular_inlines = models.BooleanField()
    collapsible_tabular_inlinef96e = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_admin_interface'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('DjangoUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoAuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_auth_group'


class DjangoAuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(DjangoAuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('DjangoAuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_auth_group_permissions'
        unique_together = (('group', 'permission'),)


class DjangoAuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    province = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_user'


class DjangoUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(DjangoUser, models.DO_NOTHING)
    group = models.ForeignKey(DjangoAuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_user_groups'
        unique_together = (('user', 'group'),)


class DjangoUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(DjangoUser, models.DO_NOTHING)
    permission = models.ForeignKey(DjangoAuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Documentaccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    document = models.BigIntegerField(blank=True, null=True)
    expiredate = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    startdocumentaccess = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentaccess'


class Failednotif(models.Model):
    id = models.BigAutoField(primary_key=True)
    createddate = models.DateTimeField(blank=True, null=True)
    retrycount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    trackingcode = models.IntegerField(blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    sender = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'failednotif'


class FcBatchContractHeader(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_template = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    file_tracking_code = models.CharField(max_length=255)
    import_date = models.DateTimeField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_batch_contract_header'


class FcContract(models.Model):
    id = models.BigAutoField(primary_key=True)
    batch_contract_header = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    import_type = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField()
    tamin_relation_id = models.BigIntegerField()
    template = models.BigIntegerField(blank=True, null=True)
    type_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_contract'


class FcContractDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    tracking_code = models.CharField(max_length=255)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_contract_document'


class FcContractExceptionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fc_contract_exception_type'


class FcContractRejectReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    reject_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fc_contract_reject_reason'


class FcContractRejectType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fc_contract_reject_type'


class FcContractTemp(models.Model):
    id = models.BigAutoField(primary_key=True)
    batch_contract_header = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    import_type = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    step = models.BigIntegerField()
    tamin_relation_id = models.BigIntegerField()
    template = models.BigIntegerField(blank=True, null=True)
    type_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_contract_temp'


class FcContractTempException(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_temp = models.BigIntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    exception_type = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_contract_temp_exception'


class FcContractTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_contract_template'


class Fileinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    trackingcode = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    upload_source = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fileinfo'


class Filetype(models.Model):
    id = models.FloatField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filetype'
        db_table_comment = '��� ����'


class Gender(models.Model):
    isactive = models.FloatField(blank=True, null=True)
    #id = models.FloatField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender'


class Graduationlevel(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'graduationlevel'


class HjApplicantJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    alleged_job = models.CharField(max_length=255, db_comment='��� ���� ����')
    alleged_role = models.CharField(max_length=255, db_comment='��� ���� ����')
    city = models.ForeignKey('Location', models.DO_NOTHING, db_column='city', db_comment='��� ')
    createdat = models.DateTimeField()
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby')
    employer_first_name = models.CharField(max_length=255, db_comment='���  �������/��������')
    employer_last_name = models.CharField(max_length=255, db_comment='���  �����ϐ� ��������/��������')
    employer_national_id = models.CharField(max_length=255, blank=True, null=True, db_comment='����� �������/��������')
    employer_phone_number = models.CharField(max_length=255, blank=True, null=True, db_comment='���� ����� �������/��������')
    insurance_list_job_title = models.CharField(max_length=255, blank=True, null=True, db_comment='����� ��� ���  ��� �� ���� ���� ')
    isic_head = models.ForeignKey('IsicActivity', models.DO_NOTHING, db_column='isic_head', blank=True, null=True, db_comment='������ ��ѐ�� (���� )')
    isic_sub_group = models.ForeignKey('IsicActivity', models.DO_NOTHING, db_column='isic_sub_group', related_name='hjapplicantjob_isic_sub_group_set', blank=True, null=True, db_comment='������ ��ѐ�� (��ѐ���)')
    job_end_date = models.DateTimeField(blank=True, null=True, db_comment='����� ����� ��� ')
    job_start_date = models.DateTimeField(db_comment='����� ���� �� ���')
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    province = models.ForeignKey('Location', models.DO_NOTHING, db_column='province', related_name='hjapplicantjob_province_set', db_comment='�����  ��� ������')
    request = models.ForeignKey('HjRequest', models.DO_NOTHING, db_column='request', db_comment='�������')
    step = models.CharField(max_length=255, db_comment='�����')
    tamin_branch = models.ForeignKey('Taminbranch', models.DO_NOTHING, db_column='tamin_branch', db_comment='���� ������ �� ����')
    version = models.BigIntegerField(blank=True, null=True)
    workshop_address = models.CharField(max_length=255, db_comment='���� ��ѐ��')
    workshop_name = models.CharField(max_length=255, db_comment='��� �ј� / ��ѐ��')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True, db_comment='����� ������� ')
    is_related_to_journalist = models.BooleanField(blank=True, null=True, db_comment='����� �� �����')
    inspection_type = models.IntegerField(blank=True, null=True, db_comment='��� ������')
    master_expert_comment = models.CharField(max_length=255, blank=True, null=True, db_comment='������� ������� �����')
    inspection = models.BooleanField(blank=True, null=True, db_comment='������ ���� ���Ͽ')
    guidance_organization = models.BooleanField(blank=True, null=True, db_comment='�� ��� ����Ͽ')
    decisionat = models.DateTimeField(blank=True, null=True)
    decisionby = models.BigIntegerField(blank=True, null=True)
    old_applicant_id = models.BigIntegerField(blank=True, null=True)
    harmful_type = models.IntegerField(blank=True, null=True)
    is_harmful = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_applicant_job'


class HjApplicantJobDoc(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicant_job = models.ForeignKey(HjApplicantJob, models.DO_NOTHING, db_column='applicant_job')
    createdat = models.DateTimeField()
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby')
    document = models.CharField(max_length=255)
    filetype = models.ForeignKey(Filetype, models.DO_NOTHING, db_column='filetype')
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_applicant_job_doc'


class HjApplicantJobHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    alleged_job = models.CharField(max_length=255)
    alleged_role = models.CharField(max_length=255)
    city = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    employer_first_name = models.CharField(max_length=255)
    employer_last_name = models.CharField(max_length=255)
    employer_national_id = models.CharField(max_length=255, blank=True, null=True)
    employer_phone_number = models.CharField(max_length=255, blank=True, null=True)
    guidance_organization = models.BooleanField()
    inspection = models.BooleanField()
    inspection_type = models.IntegerField(blank=True, null=True)
    insurance_list_job_title = models.CharField(max_length=255, blank=True, null=True)
    isic_head = models.BigIntegerField(blank=True, null=True)
    isic_sub_group = models.BigIntegerField(blank=True, null=True)
    job_end_date = models.DateTimeField(blank=True, null=True)
    job_start_date = models.DateTimeField()
    master_expert_comment = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    new_status = models.CharField(max_length=255)
    operation_at = models.DateTimeField()
    operation_by = models.BigIntegerField()
    province = models.BigIntegerField()
    request_id = models.BigIntegerField()
    step = models.CharField(max_length=255, blank=True, null=True)
    tamin_branch = models.BigIntegerField()
    role = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    workshop_address = models.CharField(max_length=255)
    workshop_name = models.CharField(max_length=255)
    zone = models.BigIntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_applicant_job_history'


class HjApplicantJobOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    alleged_job = models.CharField(max_length=255)
    alleged_role = models.CharField(max_length=255)
    city = models.ForeignKey('Location', models.DO_NOTHING, db_column='city')
    createdat = models.DateTimeField()
    createdby = models.ForeignKey('Profile', models.DO_NOTHING, db_column='createdby')
    employer_first_name = models.CharField(max_length=255)
    employer_last_name = models.CharField(max_length=255)
    employer_national_id = models.CharField(max_length=255, blank=True, null=True)
    employer_phone_number = models.CharField(max_length=255, blank=True, null=True)
    insurance_list_job_title = models.CharField(max_length=255)
    isic_head = models.ForeignKey('IsicActivity', models.DO_NOTHING, db_column='isic_head')
    isic_sub_group = models.ForeignKey('IsicActivity', models.DO_NOTHING, db_column='isic_sub_group', related_name='hjapplicantjobold_isic_sub_group_set')
    job_end_date = models.DateTimeField()
    job_start_date = models.DateTimeField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    product_head = models.BigIntegerField(blank=True, null=True)
    product_sub_group = models.BigIntegerField(blank=True, null=True)
    province = models.ForeignKey('Location', models.DO_NOTHING, db_column='province', related_name='hjapplicantjobold_province_set')
    request = models.ForeignKey('HjRequestOld', models.DO_NOTHING, db_column='request')
    step = models.CharField(max_length=255)
    tamin_branch = models.ForeignKey('Taminbranch', models.DO_NOTHING, db_column='tamin_branch')
    version = models.BigIntegerField(blank=True, null=True)
    workshop_address = models.CharField(max_length=255)
    workshop_name = models.CharField(max_length=255)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone')

    class Meta:
        managed = False
        db_table = 'hj_applicant_job_old'


class HjGuidanceOrgVote(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicant_job = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255, blank=True, null=True)
    guidance_comment = models.CharField(max_length=255)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    request = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_guidance_org_vote'


class HjHltInsReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicant_job = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    helth_inspection_report = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    pollution_measurement_report = models.CharField(max_length=255, blank=True, null=True)
    province = models.BigIntegerField()
    request = models.BigIntegerField()
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    save_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_hlt_ins_report'


class HjInspectionRefer(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicant_job = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    inspection_status = models.IntegerField()
    inspector = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    province = models.BigIntegerField()
    request = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_inspection_refer'


class HjJudgment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    province = models.BigIntegerField()
    request = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_judgment'


class HjJudgmentDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicant_job = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    employee_profile = models.BigIntegerField(blank=True, null=True)
    employee_vote_date = models.DateTimeField(blank=True, null=True)
    master_harmful_type_enum = models.IntegerField(blank=True, null=True)
    health_profile = models.BigIntegerField(blank=True, null=True)
    health_vote_date = models.DateTimeField(blank=True, null=True)
    master_is_harmful = models.BooleanField(blank=True, null=True)
    judgment = models.BigIntegerField()
    master_profile = models.BigIntegerField(blank=True, null=True)
    master_vote_date = models.DateTimeField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    province = models.BigIntegerField()
    request = models.BigIntegerField()
    tamin_profile = models.BigIntegerField(blank=True, null=True)
    tamin_vote_date = models.DateTimeField(blank=True, null=True)
    worker_profile = models.BigIntegerField(blank=True, null=True)
    worker_vote_date = models.DateTimeField(blank=True, null=True)
    employee_harmful_type_enum = models.IntegerField(blank=True, null=True)
    employee_is_harmful = models.BooleanField(blank=True, null=True)
    health_harmful_type_enum = models.IntegerField(blank=True, null=True)
    health_is_harmful = models.BooleanField(blank=True, null=True)
    tamin_harmful_type_enum = models.IntegerField(blank=True, null=True)
    tamin_is_harmful = models.BooleanField(blank=True, null=True)
    worker_harmful_type_enum = models.IntegerField(blank=True, null=True)
    worker_is_harmful = models.BooleanField(blank=True, null=True)
    judgment_text = models.TextField(blank=True, null=True)
    is_enable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_judgment_detail'


class HjRejectDocumentDefect(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    fixat = models.DateTimeField(blank=True, null=True)
    fixby = models.BigIntegerField(blank=True, null=True)
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    reject_description = models.CharField(max_length=255)
    reject_type = models.IntegerField()
    profile = models.BigIntegerField()
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_reject_document_defect'


class HjRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=4000)
    city = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_history_year = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    profile = models.BigIntegerField()
    province = models.BigIntegerField()
    status = models.IntegerField()
    tamin_branch = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    insurance_number = models.CharField(max_length=10)
    harmful_request_type = models.BooleanField(blank=True, null=True)
    refer_description = models.CharField(max_length=4000, blank=True, null=True)
    reject_description = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_request'


class HjRequestHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255)
    city = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_history_year = models.BigIntegerField()
    insurance_number = models.CharField(max_length=255)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    new_status = models.IntegerField()
    operation_at = models.DateTimeField()
    operation_by = models.BigIntegerField()
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    role = models.BigIntegerField()
    profile = models.BigIntegerField()
    province = models.BigIntegerField()
    request_id = models.BigIntegerField()
    status = models.IntegerField(blank=True, null=True)
    tamin_branch = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    refer_description = models.CharField(max_length=4000, blank=True, null=True)
    reject_description = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_request_history'


class HjRequestOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255)
    city = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_history_year = models.BigIntegerField()
    insurance_number = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    profile = models.BigIntegerField()
    province = models.BigIntegerField()
    status = models.IntegerField()
    tamin_branch = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_request_old'


class HjTaminBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    province = models.BigIntegerField()
    title = models.CharField(max_length=255)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_tamin_branch'


class HjWrkInsReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    alleged_job = models.CharField(max_length=255, blank=True, null=True)
    allowed_enter_workshop = models.BooleanField(blank=True, null=True)
    applicant_job = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    description = models.CharField(max_length=4000, blank=True, null=True)
    employer_first_name = models.CharField(max_length=255, blank=True, null=True)
    employer_last_name = models.CharField(max_length=255, blank=True, null=True)
    employer_mobile_number = models.CharField(max_length=255, blank=True, null=True)
    employer_national_code = models.CharField(max_length=255, blank=True, null=True)
    job_city = models.BigIntegerField(blank=True, null=True)
    job_province = models.BigIntegerField(blank=True, null=True)
    job_zone = models.BigIntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    province = models.BigIntegerField()
    request = models.BigIntegerField()
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    workshop_is_closed = models.BooleanField(blank=True, null=True)
    reject_description = models.CharField(max_length=255, blank=True, null=True)
    save_type = models.IntegerField(blank=True, null=True)
    job_description = models.CharField(max_length=4000, blank=True, null=True)
    harmful_factors = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hj_wrk_ins_report'


class InsAccidentAgentType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_accident_agent_type'


class InsActivityDuringAccident(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_activity_during_accident'


class InsAnnounceType(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    system_type = models.IntegerField()
    createdby = models.BigIntegerField()
    createdat = models.DateTimeField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_announce_type'


class InsAnnouncement(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    system_type = models.IntegerField(blank=True, null=True, db_comment='�� ����� �� ����� ���� 0 � �� ����� �� ����� ���� 1 ���� �� ����')
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_announcement'


class InsAnnouncementInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    updated_date = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    announce_type = models.IntegerField(blank=True, null=True)
    created_by = models.BigIntegerField()
    request_id = models.BigIntegerField(blank=True, null=True)
    sub_system = models.IntegerField(blank=True, null=True)
    tracking_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_announcement_info'


class InsByLaw(models.Model):
    #id = models.BigAutoField(primary_key=True)
    code_regulations = models.CharField(max_length=255)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description_of_regulations = models.CharField(max_length=255)
    effective_date = models.DateTimeField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    parent_code = models.CharField(max_length=255)
    violation_of_regulations = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ins_by_law'


class InsBylaws(models.Model):
    parent_code = models.CharField(max_length=8, blank=True, null=True)
    code_regulations = models.CharField(max_length=8, blank=True, null=True)
    description_of_regulations = models.TextField(blank=True, null=True)
    violation_of_regulations = models.TextField(blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    #id = models.BigAutoField()

    class Meta:
        managed = False
        db_table = 'ins_bylaws'


class InsCourtReferralReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    desciption = models.CharField(max_length=255, blank=True, null=True)
    en_key = models.CharField(max_length=255, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_court_referral_reason'


class InsInjuredBodyPart(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_injured_body_part'


class InsInjuredMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_injured_member'


class InsInjuredType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_injured_type'


class InsItemsToChecked(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=70, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_items_to_checked'


class InsJobClassification(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_job_classification'


class InsLabor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    createdby = models.BigIntegerField()
    createdat = models.DateTimeField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_labor'


class InsNumberWorkShifts(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_number_work_shifts'


class InsOfficialReferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_official_references'


class InsPlaceAccidentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_place_accident_type'


class InsReinspectionPriority(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_reinspection_priority'


class InsReportType(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    system_type = models.IntegerField()
    createdby = models.BigIntegerField()
    createdat = models.DateTimeField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_report_type'


class InsReporterPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_reporter_position'


class InsSafetyEquipment(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_safety_equipment'


class InsTimeWork(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_time_work'


class InsWelfareAmenities(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    createdby = models.BigIntegerField()
    createdat = models.DateTimeField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_welfare_amenities'


class InsWorkshopActivityFriday(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_workshop_activity_friday'


class InspDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    filetype = models.BigIntegerField()
    inspectionrequest = models.BigIntegerField()
    profile = models.BigIntegerField()
    trackingcode = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_document'


class InspReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    createdby = models.BigIntegerField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    step = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_reason'


class InspReasonReferal(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    inspection_request = models.BigIntegerField()
    referred_profile = models.BigIntegerField()
    profile = models.BigIntegerField()
    referrer_profile = models.BigIntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_reason_referal'


class InspRejectReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    inspectionrequest = models.BigIntegerField()
    rejectreason = models.BigIntegerField()
    rejector = models.BigIntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_reject_reason'


class InspRejectReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    nameen = models.CharField(max_length=255)
    namefa = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'insp_reject_reason_'


class InspRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    createdby = models.BigIntegerField()
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    step = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'insp_request'


class InspRequestReferral(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    inspection_request = models.BigIntegerField()
    position = models.IntegerField()
    profile = models.BigIntegerField()
    referrer_profile = models.BigIntegerField()
    referred_profile = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'insp_request_referral'


class InspRequestSubject(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    inspectionrequest = models.BigIntegerField()
    inspectionsubject = models.BigIntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_request_subject'


class InspSubject(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    code = models.CharField(max_length=255)
    nameen = models.CharField(max_length=255)
    namefa = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_subject'


class InspWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    address = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    employer = models.BigIntegerField(blank=True, null=True)
    faxnumber = models.CharField(max_length=255)
    identity = models.CharField(max_length=255, blank=True, null=True)
    inspectionrequest = models.BigIntegerField()
    latitude = models.FloatField(blank=True, null=True)
    location = models.BigIntegerField()
    longitude = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.CharField(max_length=255, blank=True, null=True)
    province = models.BigIntegerField()
    workshoptamininfo = models.BigIntegerField(blank=True, null=True)
    zone = models.BigIntegerField()
    employerfirstname = models.CharField(max_length=255, blank=True, null=True)
    employerlastname = models.CharField(max_length=255, blank=True, null=True)
    employernationalid = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insp_workshop'


class Insuranceconfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    eligibitycondition = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    workofficer = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insuranceconfirmation'


class Insurancedocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filetype = models.BigIntegerField()
    insurancerequest = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'insurancedocument'


class Insuranceeligibility(models.Model):
    id = models.BigAutoField(primary_key=True)
    branchofficer = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    eligibilitycondition = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insuranceeligibility'


class Insuranceeligibilitydocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    document = models.BigIntegerField(blank=True, null=True)
    insuranceeligibility = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insuranceeligibilitydocument'


class Insuranceobjection(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    insuranceobjectionlevel = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insuranceobjection'


class Insuranceobjectionlevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insuranceobjectionlevel'


class Insurancerequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    basicworkactivity = models.BigIntegerField()
    contracttype = models.BigIntegerField()
    createdate = models.DateTimeField()
    createdby = models.BigIntegerField()
    dependentsnumber = models.BigIntegerField()
    education = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    indictment = models.BigIntegerField(blank=True, null=True)
    insurancedurationbeforeunemploymentmonth = models.BigIntegerField()
    insurancedurationinlastworkshopmonth = models.BigIntegerField()
    is_b_band = models.BooleanField(blank=True, null=True)
    lastjob = models.CharField(max_length=255)
    lastencyday = models.BigIntegerField()
    location = models.BigIntegerField()
    militaryservicecardnumber = models.CharField(max_length=255, blank=True, null=True)
    militaryservicestatus = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    step = models.CharField(max_length=255)
    taminworkshopcode = models.CharField(max_length=255, blank=True, null=True)
    unemploymentreason = models.BigIntegerField()
    unemploymentstartdate = models.DateTimeField()
    workskilllevel = models.BigIntegerField()
    workshopaddress = models.CharField(max_length=255)
    workshopname = models.CharField(max_length=255)
    workshoppostalcode = models.CharField(max_length=255, blank=True, null=True)
    zone = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'insurancerequest'


class Insurancerequesthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    basicworkactivity = models.BigIntegerField()
    contracttype = models.BigIntegerField()
    createdate = models.DateTimeField()
    createdby = models.BigIntegerField()
    dependentsnumber = models.BigIntegerField()
    iban = models.CharField(max_length=255)
    indictment = models.BigIntegerField(blank=True, null=True)
    insurancedurationbeforeunemploymentmonth = models.BigIntegerField()
    insurancedurationinlastworkshopmonth = models.BigIntegerField()
    insurance_request_id = models.BigIntegerField()
    lastjob = models.CharField(max_length=255)
    lastencyday = models.BigIntegerField()
    location = models.BigIntegerField()
    militaryservicecardnumber = models.CharField(max_length=255, blank=True, null=True)
    militaryservicestatus = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    operation_at = models.DateTimeField(blank=True, null=True)
    operation_by = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    step = models.CharField(max_length=255)
    taminworkshopcode = models.CharField(max_length=255, blank=True, null=True)
    unemploymentreason = models.BigIntegerField()
    unemploymentstartdate = models.DateTimeField()
    workskilllevel = models.BigIntegerField()
    workshopaddress = models.CharField(max_length=255)
    workshopname = models.CharField(max_length=255)
    workshoppostalcode = models.CharField(max_length=255, blank=True, null=True)
    zone = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'insurancerequesthistory'


class Insurancereview(models.Model):
    id = models.BigAutoField(primary_key=True)
    cheifofficer = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    eligibitycondition = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurancereview'


class Isco(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_code = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isco'


class IsicActivity(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    parent_id = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'isic_activity'


class Jobtitletype(models.Model):
    id = models.FloatField(primary_key=True)
    parentid = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobtitletype'


class LegalArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    bylaws = models.BigIntegerField()
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'legal_article'
        unique_together = (('bylaws', 'code'),)


class Location(models.Model):
    isfreeconomiczone = models.FloatField(blank=True, null=True)
    isspecialeconomiczone = models.FloatField(blank=True, null=True)
    id = models.FloatField(primary_key=True)
    locationtype = models.FloatField(blank=True, null=True)
    parentid = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    prefixcode = models.CharField(max_length=255, blank=True, null=True)

    @classmethod
    def get_top_level_locations(cls):
        """Return locations where `parentid` is null."""
        return cls.objects.filter(parentid__isnull=True)

    def get_parent(self):
        """Return the parent location."""
        if self.parentid is not None:
            return Location.objects.filter(id=self.parentid).first()
        return None

    def __str__(self):
        parent_location = self.get_parent()
        parent_name = parent_location.name if parent_location else 'No parent'
        return f"{self.name} ({parent_name})"

    class Meta:
        managed = False
        db_table = 'location'


# class Location(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     locationtype = models.BooleanField(blank=True, null=True)
#     parentid = models.IntegerField(blank=True, null=True)
#     parentcode = models.CharField(max_length=6, blank=True, null=True)
#     code = models.CharField(max_length=6)
#     name = models.CharField(max_length=50)
#     prefixcode = models.CharField(max_length=255, blank=True, null=True)
#     isfreeconomiczone = models.FloatField(blank=True, null=True)
#     isspecialeconomiczone = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'location_'


class LocationOpr(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code_convert = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_opr'


class Locationtype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locationtype'


class Maritalstatus(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maritalstatus'


class MilitaryInfo(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'military_info'


class Militaryservicestatus(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'militaryservicestatus'


class Nationality(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    isctizenship = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nationality'


class ObjectionRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    master_description = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    objection_description = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objection_request'


class Office(models.Model):
    #id = models.BigAutoField()
    code = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    ishqoffice = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    parentid = models.BigIntegerField(blank=True, null=True)
    economical_code = models.CharField(max_length=255, blank=True, null=True)
    english_name = models.CharField(max_length=255, blank=True, null=True)
    fax_number = models.CharField(max_length=255, blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    national_code = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    registry_date = models.DateTimeField(blank=True, null=True)
    registry_number = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    zone_id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    office_role = models.BigIntegerField(blank=True, null=True)
    ownership = models.BigIntegerField(blank=True, null=True)
    municipal_zone_code = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office'

    def __str__(self):
        return self.name


class OfficeRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    type_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_role'


class OfficeSupport(models.Model):
    id = models.BigAutoField(primary_key=True)
    committee_type = models.BigIntegerField()
    created_at = models.DateTimeField()
    createdby = models.BigIntegerField()
    is_active = models.BooleanField()
    modified_at = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField()
    supported_office = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_support'


class Officelocationsupport(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    location = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    zone = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'officelocationsupport'
        unique_together = (('location', 'office', 'zone', 'isactive'),)


class Officestaff(models.Model):
    id = models.BigAutoField(primary_key=True)
    activrfrom = models.DateTimeField(blank=True, null=True)
    activrto = models.DateTimeField(blank=True, null=True)
    committee = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    office = models.ForeignKey('Office', models.DO_NOTHING, db_column='office', blank=True, null=True, verbose_name='اداره')
    profile = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile', blank=True, null=True, verbose_name='پروفایل')
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='role', blank=True, null=True, verbose_name='نقش')
    committeebranch = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'officestaff'
        verbose_name = 'اداره'
        verbose_name_plural = 'ادارات سازمانی'


class OfficialReference(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'official_reference'


class OwnershipType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ownership_type'


class Permission(models.Model):
    generalpermission = models.FloatField(blank=True, null=True)
    id = models.FloatField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enkey = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class Physicalcondition(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physicalcondition'


class Position(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    parent_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    deathdate = models.DateField(blank=True, null=True, verbose_name='تاریخ فوت')
    isactive = models.BigIntegerField(default=1, blank=True, null=True, verbose_name='وضعیت کاربر')
    activefrom = models.DateTimeField(blank=True, null=True, verbose_name='فعال از')
    activeto = models.DateTimeField(blank=True, null=True, verbose_name='فعال تا')
    childrennumber = models.BigIntegerField(blank=True, null=True, verbose_name='تعداد فرزند')
    createdat = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ ایجاد')
    createdby = models.BigIntegerField(default=1, blank=True, null=True, verbose_name='ایجاد شده توسط')
    defunctdate = models.BigIntegerField(blank=True, null=True, verbose_name='')
    foundationdate = models.BigIntegerField(blank=True, null=True, verbose_name='')
    gender = models.BigIntegerField(blank=True, null=True, verbose_name='کد جنسیت')
    graduation = models.BigIntegerField(blank=True, null=True, verbose_name='سطح تحصیلات')
    location = models.BigIntegerField(blank=True, null=True, verbose_name='کد شهر')
    maritalstatus = models.BigIntegerField(blank=True, null=True, verbose_name='وضعیت تاهل')
    modifiedat = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='تاریخ بروزرسانی')
    #last_login = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='تاریخ بروزرسانی')
    modifiedby = models.BigIntegerField(blank=True, null=True, verbose_name='بروزرسانی شده')
    religion = models.BigIntegerField(blank=True, null=True, verbose_name='مذهب')
    postalcode = models.CharField(max_length=10, blank=True, null=True, verbose_name='کدپستی')
    zonecode = models.CharField(max_length=10, blank=True, null=True, verbose_name='منطقه')
    FOREIGNERID = models.CharField(max_length=12, blank=True, null=True, verbose_name='')
    NATIONALID = models.CharField(max_length=12, blank=True, null=True, verbose_name='کدملی')
    faxnumber = models.CharField(max_length=20, blank=True, null=True, verbose_name='نمابر')
    mobilenumber = models.CharField(max_length=20, blank=True, null=True, verbose_name='تلفن همراه')
    nationalcertificatecode = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره شناسنامه')
    nationalcertificateserial = models.CharField(max_length=20, blank=True, null=True, verbose_name='سریال شناسنامه')
    phonenumber = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره ثابت')
    fathername = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام پدر')
    firstname = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام')
    lastname = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام خانوادگی')
    organizationname = models.CharField(max_length=50, blank=True, null=True, verbose_name='سازمان')
    password = models.CharField(max_length=100, blank=True, null=True, verbose_name='کلمه عبور')
    username = models.CharField(unique=True, max_length=50, blank=True, null=True, verbose_name='نام کاربری')
    address = models.CharField(max_length=1000, blank=True, null=True, verbose_name='آدرس')
    secretkey = models.CharField(max_length=4000, blank=True, null=True, verbose_name='کلید رمز')
    birthdate = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ تولد')
    currenttaminworkshopcode = models.CharField(max_length=255, blank=True, null=True, verbose_name='')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='آدرس پستی')
    graduationlevel = models.CharField(max_length=255, blank=True, null=True, verbose_name='سطح تحصیل')
    physicalcondition = models.CharField(max_length=255, blank=True, null=True, verbose_name='وضعیت جسمانی')
    idno = models.CharField(max_length=255, blank=True, null=True, verbose_name='شماره آیدی')
    ispermittedtoreceivebyemail = models.BigIntegerField(blank=True, null=True, verbose_name='دریافت پست الکترونیکی')
    ispermittedtoreceivebyfax = models.BigIntegerField(blank=True, null=True, verbose_name='دریافت نمابر')
    militaryservicestatus = models.BigIntegerField(blank=True, null=True, verbose_name='وضعیت خدمت سربازی')
    parentlocation = models.BigIntegerField(blank=True, null=True, verbose_name='استان')
    nationality = models.CharField(max_length=255, blank=True, null=True, verbose_name='ملیت')
    usertype = models.ForeignKey('Roletype', models.DO_NOTHING, db_column='usertype', blank=True, null=True, verbose_name='نوع کاربر')
    officialemail = models.CharField(max_length=255, blank=True, null=True, verbose_name='پست الکترونیک')
    externalusertype = models.IntegerField(blank=True, null=True, verbose_name='نوع کاربر خارجی')
    is_converted = models.BigIntegerField(blank=True, null=True, verbose_name='داده کانورت شده')
    birth_place = models.BigIntegerField(blank=True, null=True, verbose_name='محل تولد')
    force_password_change = models.BooleanField(default =True, blank=True, null=True, verbose_name='وضعیت تعویض کلمه عبور')
    force_profile_completion = models.BooleanField(default =True, blank=True, null=True, verbose_name='وضعیت تکمیل پروفایل')

    class Meta:
        managed = False
        db_table = 'profile'
        verbose_name='پروفایل'
        verbose_name_plural = 'پروفایل'

    def __str__(self):
        return self.username


class Profilepermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    expiredate = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilepermission'


class Profilerole(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile', related_name='profileroles', blank=True, null=True, verbose_name='پروفایل')
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='role', blank=True, null=True, verbose_name='نقش')
    isactive = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    is_default = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilerole'
        verbose_name = 'نقش پروفایل'
        verbose_name_plural = 'نقش های پروفایل'

    def __str__(self):
        return str(self.profile)


class Provincecommitteejudgment(models.Model):
    id = models.BigAutoField(primary_key=True)
    committee = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    provincechiefofficer = models.BigIntegerField(blank=True, null=True)
    provincechiefofficerdescription = models.CharField(max_length=255, blank=True, null=True)
    provincechiefofficereligibilitycondition = models.BigIntegerField(blank=True, null=True)
    taminprovincecheifofficerdescription = models.CharField(max_length=255, blank=True, null=True)
    taminprovincecheiefofficer = models.BigIntegerField(blank=True, null=True)
    taminprovinceofficereligibilitycondition = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincecommitteejudgment'


class RejectDocumentDefect(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    fixat = models.DateTimeField(blank=True, null=True)
    fixby = models.BigIntegerField(blank=True, null=True)
    fixdescription = models.CharField(max_length=255, blank=True, null=True)
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    reject_description = models.CharField(db_column='reject description', max_length=255)  # Field renamed to remove unsuitable characters.
    reject_type = models.IntegerField()
    profile = models.BigIntegerField()
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reject_document_defect'


class RejectReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    nameen = models.CharField(max_length=255)
    namefa = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reject_reason'


class Religion(models.Model):
    #id = models.BigIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'religion'


class Reportbundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    profileid = models.BigIntegerField(blank=True, null=True)
    qrcodetypeenum = models.IntegerField()
    reportid = models.BigIntegerField()
    trackingcode = models.CharField(max_length=100)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportbundle'


class Request(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    currentworkflowstate = models.BigIntegerField(blank=True, null=True)
    currentworkflowstep = models.BigIntegerField(blank=True, null=True)
    finalized = models.BooleanField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    requesttype = models.BigIntegerField(blank=True, null=True)
    requester = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request'


class Requestcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    requester = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestcode'


class Requesttype(models.Model):
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.FloatField(blank=True, null=True)
    #id = models.FloatField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requesttype'


class Role(models.Model):
    createdat = models.DateTimeField()
    createdby = models.FloatField()
    id = models.FloatField(primary_key=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    enkey = models.CharField(max_length=50)
    roletype = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'role'

    def __str__(self):
        return self.name


class Rolepermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.BigIntegerField(blank=True, null=True)
    permission = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.IntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolepermission'


class Rolepermission(models.Model):
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.FloatField(blank=True, null=True)
    id = models.FloatField(primary_key=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    permission = models.FloatField(blank=True, null=True)
    role = models.FloatField(blank=True, null=True)
    isactive = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolepermission_'


class Roletype(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.IntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roletype'

    def __str__(self):
        return self.name


class SafetyEquipment(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_equipment'


class Speciallisttype(models.Model):
    isactive = models.FloatField(blank=True, null=True)
    #id = models.FloatField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speciallisttype'


class SsoLegalAccountInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    fax_number = models.CharField(max_length=255, blank=True, null=True)
    fix_phone_number = models.CharField(max_length=255, blank=True, null=True)
    issuance_date = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    national_id = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    register_date = models.CharField(max_length=255, blank=True, null=True)
    register_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sso_legal_account_info'


class TaminAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    assigndate = models.DateTimeField(blank=True, null=True)
    branch = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tamin_assignment'


class TaminContractRow(models.Model):
    id = models.BigAutoField(primary_key=True)
    character = models.CharField(max_length=255, blank=True, null=True)
    contract_row = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    workshop_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tamin_contract_row'


class TaminEmployerRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_row = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    createdby = models.BigIntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    national_code = models.CharField(max_length=255)
    profile = models.BigIntegerField()
    workshop_code = models.CharField(max_length=255)
    is_active = models.BooleanField()
    covonent_id = models.BigIntegerField(blank=True, null=True)
    workshop_id = models.CharField(max_length=255)
    created_by = models.BigIntegerField()
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tamin_employer_relation'


class TaminMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tamin_member'


class TaminTwoYearEnquiry(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    history_type_desc = models.CharField(max_length=255, blank=True, null=True)
    history_year = models.CharField(max_length=255, blank=True, null=True)
    insurance_id = models.BigIntegerField(blank=True, null=True)
    month01 = models.CharField(max_length=255, blank=True, null=True)
    month02 = models.CharField(max_length=255, blank=True, null=True)
    month03 = models.CharField(max_length=255, blank=True, null=True)
    month04 = models.CharField(max_length=255, blank=True, null=True)
    month05 = models.CharField(max_length=255, blank=True, null=True)
    month06 = models.CharField(max_length=255, blank=True, null=True)
    month07 = models.CharField(max_length=255, blank=True, null=True)
    month08 = models.CharField(max_length=255, blank=True, null=True)
    month09 = models.CharField(max_length=255, blank=True, null=True)
    month10 = models.CharField(max_length=255, blank=True, null=True)
    month11 = models.CharField(max_length=255, blank=True, null=True)
    month12 = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    workshop_id = models.BigIntegerField(blank=True, null=True)
    workshop_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tamin_two_year_enquiry'


class TaminWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    character = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    workshop_code = models.CharField(max_length=255, blank=True, null=True)
    workshop_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tamin_workshop'


class Taminbranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    location = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    zone = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taminbranch'


class Taminbranchofficer(models.Model):
    id = models.BigAutoField(primary_key=True)
    isactive = models.CharField(max_length=1, blank=True, null=True)
    activefrom = models.DateTimeField(blank=True, null=True)
    activeto = models.DateTimeField()
    branch = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField()
    modifiedby = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'taminbranchofficer'


class Taminmaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    activrfrom = models.DateTimeField(blank=True, null=True)
    activrto = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    ishqcheifofficer = models.BooleanField(blank=True, null=True)
    location = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taminmaster'


class Test(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Trialcommitteejudgment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    judgmenttext = models.BigIntegerField(blank=True, null=True)
    judgmenttype = models.BigIntegerField(blank=True, null=True)
    minutedocument = models.BigIntegerField(blank=True, null=True)
    minutesummery = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    savetype = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trialcommitteejudgment'


class UnCommitteeCalendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.BigIntegerField(blank=True, null=True)
    committee = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    insurance_request = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_committee_calendar'


class UnCommitteeMemberVote(models.Model):
    id = models.BigAutoField(primary_key=True)
    agreement = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    has_done = models.BooleanField(blank=True, null=True)
    judgment = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    trialcommitteemember = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_committee_member_vote'


class UnCommitteemember(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeearrangement = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    committee = models.BigIntegerField(blank=True, null=True)
    unemploymentcommittee = models.BigIntegerField(blank=True, null=True)
    hasdone = models.BooleanField(blank=True, null=True)
    rolecall = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_committeemember'


class UnDocumentDefectDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    file_id = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255)
    reject_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_document_defect_detail'


class UnInsurancedocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filetype = models.BigIntegerField()
    insurancerequest = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_insurancedocument'


class UnInsuranceobjection(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    insuranceobjectionlevel = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_insuranceobjection'


class UnInsurancerequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    basicworkactivity = models.BigIntegerField()
    contracttype = models.BigIntegerField()
    createdate = models.DateTimeField()
    createdby = models.BigIntegerField()
    dependentsnumber = models.BigIntegerField()
    iban = models.CharField(max_length=24)
    indictment = models.BigIntegerField(blank=True, null=True)
    insurancedurationbeforeunemploymentmonth = models.BigIntegerField()
    insurancedurationinlastworkshopmonth = models.BigIntegerField()
    is_b_band = models.BooleanField(blank=True, null=True)
    lastjob = models.CharField(max_length=255)
    lastencyday = models.BigIntegerField()
    location = models.BigIntegerField()
    militaryservicecardnumber = models.CharField(max_length=255, blank=True, null=True)
    militaryservicestatus = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    step = models.CharField(max_length=255)
    taminworkshopcode = models.CharField(max_length=255, blank=True, null=True)
    unemploymentreason = models.BigIntegerField()
    unemploymentstartdate = models.DateTimeField()
    workskilllevel = models.BigIntegerField()
    workshopaddress = models.CharField(max_length=255)
    workshopname = models.CharField(max_length=255)
    workshoppostalcode = models.CharField(max_length=255, blank=True, null=True)
    zone = models.BigIntegerField()
    education = models.CharField(max_length=255, blank=True, null=True)
    complaint = models.BigIntegerField(blank=True, null=True)
    complaint_register_date = models.DateField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    sent_to_stp_at = models.DateTimeField(blank=True, null=True)
    sent_to_stp_by = models.BigIntegerField(blank=True, null=True)
    stp_tracking_code = models.BigIntegerField(blank=True, null=True)
    insurance_number = models.CharField(max_length=10)
    bank = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_insurancerequest'


class UnInsurancerequesthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    basicworkactivity = models.BigIntegerField()
    contracttype = models.BigIntegerField()
    createdate = models.DateTimeField()
    createdby = models.BigIntegerField()
    dependentsnumber = models.BigIntegerField()
    iban = models.CharField(max_length=255)
    indictment = models.BigIntegerField(blank=True, null=True)
    insurancedurationbeforeunemploymentmonth = models.BigIntegerField()
    insurancedurationinlastworkshopmonth = models.BigIntegerField()
    insurance_request_id = models.BigIntegerField()
    lastjob = models.CharField(max_length=255)
    lastencyday = models.BigIntegerField()
    location = models.BigIntegerField()
    militaryservicecardnumber = models.CharField(max_length=255, blank=True, null=True)
    militaryservicestatus = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    operation_at = models.DateTimeField(blank=True, null=True)
    operation_by = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    step = models.CharField(max_length=255)
    taminworkshopcode = models.CharField(max_length=255, blank=True, null=True)
    unemploymentreason = models.BigIntegerField()
    unemploymentstartdate = models.DateTimeField()
    workskilllevel = models.BigIntegerField()
    workshopaddress = models.CharField(max_length=255)
    workshopname = models.CharField(max_length=255)
    workshoppostalcode = models.CharField(max_length=255, blank=True, null=True)
    zone = models.BigIntegerField()
    account_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_insurancerequesthistory'


class UnJudgment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    judgmenttext = models.TextField()
    judgmenttype = models.BigIntegerField()
    minutesdocument = models.CharField(max_length=255)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    savetype = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_judgment'


class UnObjectionDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    document = models.CharField(max_length=255)
    filetype = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_objection_document'


class UnObjectionReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    master_description = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    objection_description = models.CharField(max_length=255, blank=True, null=True)
    objection_step = models.CharField(max_length=255)
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_objection_reason'


class UnObjectionRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    objection_description = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    master_description = models.CharField(max_length=255, blank=True, null=True)
    objection_step = models.CharField(max_length=255)
    center_description = models.CharField(max_length=255, blank=True, null=True)
    province_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_objection_request'


class UnOpinionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    cycle = models.BigIntegerField(blank=True, null=True)
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    vote = models.BooleanField(blank=True, null=True)
    opinion_type = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    opinion = models.BooleanField(blank=True, null=True)
    labor_department_comment = models.CharField(max_length=255, blank=True, null=True)
    social_security_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_opinion_detail'


class UnRejectDocumentDefect(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    reject_description = models.CharField(max_length=255)
    version = models.BigIntegerField(blank=True, null=True)
    fixat = models.DateTimeField(blank=True, null=True)
    fixby = models.BigIntegerField(blank=True, null=True)
    fixdescription = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    reject_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_reject_document_defect'


class UnSalaryCutoff(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    cutoff_reason = models.BigIntegerField()
    description = models.CharField(max_length=255)
    insurance_request = models.BigIntegerField()
    salary_head_id = models.BigIntegerField()
    stp_result_id = models.BigIntegerField()
    position = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_salary_cutoff'


class UnSalaryCutoffReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_salary_cutoff_reason'


class UnSalaryDetailList(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    salary_head_id = models.BigIntegerField()
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    tamin_branch = models.BigIntegerField()
    profile = models.BigIntegerField()
    stp_request_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_salary_detail_list'


class UnSalaryHeadList(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    month = models.IntegerField()
    office = models.BigIntegerField()
    send_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_salary_head_list'


class UnStpRequestResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.BigIntegerField()
    average_salary = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    end_date = models.DateTimeField()
    file_number = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    insurance_number = models.CharField(max_length=255)
    insurance_request = models.BigIntegerField()
    location = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    national_code = models.CharField(max_length=255)
    period_of_having_right_month = models.BigIntegerField(blank=True, null=True)
    response_text = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    start_of_unemployment = models.DateTimeField()
    status = models.IntegerField()
    stp_response_status = models.IntegerField()
    tamin_branch = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    period_of_having_right_day = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField()
    zone = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_stp_request_result'


class UnTaminAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    assigndate = models.DateTimeField(blank=True, null=True)
    branch = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_tamin_assignment'


class UnTaminMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.BigIntegerField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    profile = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_tamin_member'


class UnTaminTwoYearEnquiry(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    history_type_desc = models.CharField(max_length=255, blank=True, null=True)
    history_year = models.CharField(max_length=255, blank=True, null=True)
    insurance_id = models.BigIntegerField(blank=True, null=True)
    month01 = models.CharField(max_length=255, blank=True, null=True)
    month02 = models.CharField(max_length=255, blank=True, null=True)
    month03 = models.CharField(max_length=255, blank=True, null=True)
    month04 = models.CharField(max_length=255, blank=True, null=True)
    month05 = models.CharField(max_length=255, blank=True, null=True)
    month06 = models.CharField(max_length=255, blank=True, null=True)
    month07 = models.CharField(max_length=255, blank=True, null=True)
    month08 = models.CharField(max_length=255, blank=True, null=True)
    month09 = models.CharField(max_length=255, blank=True, null=True)
    month10 = models.CharField(max_length=255, blank=True, null=True)
    month11 = models.CharField(max_length=255, blank=True, null=True)
    month12 = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    workshop_id = models.BigIntegerField(blank=True, null=True)
    workshop_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_tamin_two_year_enquiry'


class UnTransferRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    insurance_request = models.BigIntegerField()
    file_number = models.CharField(max_length=50, blank=True, null=True)
    source_office = models.BigIntegerField()
    target_office = models.BigIntegerField()
    source_tamin_branch = models.BigIntegerField()
    target_tamin_branch = models.BigIntegerField()
    status = models.IntegerField()
    transfer_date = models.DateTimeField(blank=True, null=True)
    approve_transfer_date = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    approve_at = models.DateTimeField(blank=True, null=True)
    approve_by = models.BigIntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_transfer_request'


class UnTrialcommitteejudgment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    insurancerequest = models.BigIntegerField(blank=True, null=True)
    judgmenttext = models.BigIntegerField(blank=True, null=True)
    judgmenttype = models.BigIntegerField(blank=True, null=True)
    minutedocument = models.BigIntegerField(blank=True, null=True)
    minutesummery = models.CharField(max_length=255, blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    savetype = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_trialcommitteejudgment'


class UnTrialvote(models.Model):
    id = models.BigAutoField(primary_key=True)
    agreement = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    judgment = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    trialcommitteemember = models.BigIntegerField(blank=True, null=True)
    has_done = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'un_trialvote'


class UnUnemploymentCommittee(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.BigIntegerField(blank=True, null=True)
    committee = models.BigIntegerField()
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    insurance_request = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'un_unemployment_committee'


class UnUnemploymentreason(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    reasontype = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'un_unemploymentreason'
# Unable to inspect table 'un_unemploymentreasoncontracttypesupport'
# The error was: ORA-00942: table or view does not exist



class Unemploymentreason(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    reasontype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unemploymentreason'
# Unable to inspect table 'unemploymentreasoncontracttypesupport'
# The error was: ORA-00942: table or view does not exist



class Usertype(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField()
    createdby = models.IntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usertype'


class WorkShift(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_shift'


class WorkSkillLevel(models.Model):
    #id = models.BigIntegerField()
    lvl = models.BigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_skill_level'


class Workflowrequesthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    fromworkflowstep = models.BigIntegerField(blank=True, null=True)
    fromworkflowstate = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    performedby = models.BigIntegerField(blank=True, null=True)
    request = models.BigIntegerField(blank=True, null=True)
    toworkflowstate = models.BigIntegerField(blank=True, null=True)
    toworkflowstep = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflowrequesthistory'


class Workflowstate(models.Model):
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.FloatField(blank=True, null=True)
    #id = models.FloatField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.FloatField(blank=True, null=True)
    workflow = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflowstate'


class Workflowstep(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    workflowstate = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflowstep'


class WorkshopInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    updated_date = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    address = models.CharField(max_length=255)
    city = models.BigIntegerField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    province = models.BigIntegerField()
    zone = models.BigIntegerField()
    city_name = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.CharField(max_length=255, blank=True, null=True)
    province_name = models.CharField(max_length=255, blank=True, null=True)
    zone_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_info'


class WorkshopLegalType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_legal_type'


class WorkshopStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    createdby = models.BigIntegerField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_status'


class WorkshopTaminInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdat = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    modifiedat = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    address = models.CharField(max_length=255)
    document = models.BigIntegerField()
    faxnumber = models.CharField(max_length=255)
    identity = models.CharField(max_length=255, blank=True, null=True)
    inquiry_date = models.DateTimeField(blank=True, null=True)
    inspectionsubject = models.BigIntegerField()
    latitude = models.FloatField(blank=True, null=True)
    location = models.BigIntegerField()
    longitude = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.CharField(max_length=255, blank=True, null=True)
    province = models.BigIntegerField()
    zone = models.BigIntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_tamin_info'


class Workskilllevel_second(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    lvl = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workskilllevel'


class WrsSubsystems(models.Model):
    id = models.FloatField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wrs_subsystems'


class WrsSubsystemsSteps(models.Model):
    id = models.FloatField(primary_key=True)
    step_full_code = models.CharField(max_length=20, blank=True, null=True)
    step_description_fa = models.CharField(max_length=100, blank=True, null=True)
    subsystem_id = models.FloatField(blank=True, null=True)
    step_description_en = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wrs_subsystems_steps'


class WrsSubsystemsWorkflow(models.Model):
    id = models.FloatField(primary_key=True)
    current_step_code = models.CharField(max_length=100)
    upcoming_step_code = models.CharField(max_length=100)
    subsystem_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wrs_subsystems_workflow'


class Zone(models.Model):
    #id = models.FloatField(primary_key=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='location', blank=True, null=True, verbose_name='شهر')
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name='کد منطقه')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام منطقه')

    class Meta:
        managed = False
        db_table = 'zone'
        verbose_name='منطقه شهرداری'
        verbose_name_plural = 'مناطق شهرداری'

    def __str__(self):
        return self.name


class Zone_second(models.Model):
    province_id = models.CharField(max_length=40)
    province_enum = models.CharField(max_length=40, blank=True, null=True)
    province_name = models.CharField(max_length=4000, blank=True, null=True)
    city_id = models.CharField(max_length=40)
    city_enum = models.CharField(max_length=40, blank=True, null=True)
    city_name = models.CharField(max_length=4000, blank=True, null=True)
    municipality_id = models.CharField(max_length=40)
    municipality_enum = models.CharField(max_length=40, blank=True, null=True)
    municipality_name = models.CharField(max_length=4000, blank=True, null=True)
    #id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone_'
