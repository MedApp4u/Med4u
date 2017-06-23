# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 11:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyHealthApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_address',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_pic',
            field=models.ImageField(blank=True, null=True, upload_to='doctors'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_speciality',
            field=models.CharField(blank=True, choices=[(b'ADDICTION PSYCHIATRIST', b'Addiction psychiatrist'), (b'ADOLESCENT MEDICINE SPECIALIST', b'Adolescent medicine specialist'), (b'ALLERGIST (IMMUNOLOGIST)', b'Allergist (immunologist)'), (b'ANESTHESIOLOGIST', b'Anesthesiologist'), (b'CARDIAC ELECTROPHYSIOLOGIST', b'Cardiac electrophysiologist'), (b'CARDIOLOGIST', b'Cardiologist'), (b'CARDIOVASCULAR SURGEON', b'Cardiovascular surgeon'), (b'COLON ', b'Colon '), (b'CRITICAL CARE MEDICINE SPECIALIST', b'Critical care medicine specialist'), (b'DERMATOLOGIST', b'Dermatologist'), (b'DEVELOPMENTAL PEDIATRICIAN', b'Developmental pediatrician'), (b'EMERGENCY MEDICINE SPECIALIST', b'Emergency medicine specialist'), (b'ENDOCRINOLOGIST', b'Endocrinologist'), (b'FAMILY MEDICINE PHYSICIAN', b'Family medicine physician'), (b'FORENSIC PATHOLOGIST', b'Forensic pathologist'), (b'GASTROENTEROLOGIST', b'Gastroenterologist'), (b'GERIATRIC MEDICINE SPECIALIST', b'Geriatric medicine specialist'), (b'GYNECOLOGIST', b'Gynecologist'), (b'GYNECOLOGIC ONCOLOGIST', b'Gynecologic oncologist'), (b'HAND SURGEON', b'Hand surgeon'), (b'HEMATOLOGIST', b'Hematologist'), (b'HEPATOLOGIST', b'Hepatologist'), (b'HOSPITALIST', b'Hospitalist'), (b'HOSPICE ', b'Hospice '), (b'HYPERBARIC PHYSICIAN', b'Hyperbaric physician'), (b'INFECTIOUS DISEASE SPECIALIST', b'Infectious disease specialist'), (b'INTERNIST', b'Internist'), (b'INTERVENTIONAL CARDIOLOGIST', b'Interventional cardiologist'), (b'MEDICAL EXAMINER', b'Medical examiner'), (b'MEDICAL GENETICIST', b'Medical geneticist'), (b'NEONATOLOGIST', b'Neonatologist'), (b'NEPHROLOGIST', b'Nephrologist'), (b'NEUROLOGICAL SURGEON', b'Neurological surgeon'), (b'NEUROLOGIST', b'Neurologist'), (b'NUCLEAR MEDICINE SPECIALIST', b'Nuclear medicine specialist'), (b'OBSTETRICIAN', b'Obstetrician'), (b'OCCUPATIONAL MEDICINE SPECIALIST', b'Occupational medicine specialist'), (b'ONCOLOGIST', b'Oncologist'), (b'OPHTHALMOLOGIST', b'Ophthalmologist'), (b'ORAL SURGEON ', b'Oral surgeon '), (b'ORTHOPEDIC SURGEON', b'Orthopedic surgeon'), (b'OTOLARYNGOLOGIST', b'Otolaryngologist'), (b'PAIN MANAGEMENT SPECIALIST', b'Pain management specialist'), (b'PATHOLOGIST', b'Pathologist'), (b'PEDIATRICIAN', b'Pediatrician'), (b'PERINATOLOGIST', b'Perinatologist'), (b'PHYSIATRIST', b'Physiatrist'), (b'PLASTIC SURGEON', b'Plastic surgeon'), (b'PSYCHIATRIST', b'Psychiatrist'), (b'PULMONOLOGIST', b'Pulmonologist'), (b'RADIATION ONCOLOGIST', b'Radiation oncologist'), (b'RADIOLOGIST', b'Radiologist'), (b'REPRODUCTIVE ENDOCRINOLOGIST', b'Reproductive endocrinologist'), (b'RHEUMATOLOGIST', b'Rheumatologist'), (b'SLEEP DISORDERS SPECIALIST', b'Sleep disorders specialist'), (b'SPINAL CORD INJURY SPECIALIST', b'Spinal cord injury specialist'), (b'SPORTS MEDICINE SPECIALIST', b'Sports medicine specialist'), (b'SURGEON', b'Surgeon'), (b'THORACIC SURGEON', b'Thoracic surgeon'), (b'UROLOGIST', b'Urologist'), (b'VASCULAR SURGEON', b'Vascular surgeon')], default='FAMILY MEDICINE PHYSICIAN', max_length=60),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]