# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 09:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyHealthApp', '0014_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(default=False, max_length=1000),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='mobile',
            field=models.BigIntegerField(default=9999999999L, validators=[django.core.validators.MaxValueValidator(9999999999L), django.core.validators.MinValueValidator(1000000000)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='Enter Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('ADDICTION PSYCHIATRIST', 'Addiction psychiatrist'), ('ADOLESCENT MEDICINE SPECIALIST', 'Adolescent medicine specialist'), ('ALLERGIST (IMMUNOLOGIST)', 'Allergist (immunologist)'), ('ANESTHESIOLOGIST', 'Anesthesiologist'), ('CARDIAC ELECTROPHYSIOLOGIST', 'Cardiac electrophysiologist'), ('CARDIOLOGIST', 'Cardiologist'), ('CARDIOVASCULAR SURGEON', 'Cardiovascular surgeon'), ('COLON ', 'Colon '), ('CRITICAL CARE MEDICINE SPECIALIST', 'Critical care medicine specialist'), ('DERMATOLOGIST', 'Dermatologist'), ('DEVELOPMENTAL PEDIATRICIAN', 'Developmental pediatrician'), ('EMERGENCY MEDICINE SPECIALIST', 'Emergency medicine specialist'), ('ENDOCRINOLOGIST', 'Endocrinologist'), ('FAMILY MEDICINE PHYSICIAN', 'Family medicine physician'), ('FORENSIC PATHOLOGIST', 'Forensic pathologist'), ('GASTROENTEROLOGIST', 'Gastroenterologist'), ('GERIATRIC MEDICINE SPECIALIST', 'Geriatric medicine specialist'), ('GYNECOLOGIST', 'Gynecologist'), ('GYNECOLOGIC ONCOLOGIST', 'Gynecologic oncologist'), ('HAND SURGEON', 'Hand surgeon'), ('HEMATOLOGIST', 'Hematologist'), ('HEPATOLOGIST', 'Hepatologist'), ('HOSPITALIST', 'Hospitalist'), ('HOSPICE ', 'Hospice '), ('HYPERBARIC PHYSICIAN', 'Hyperbaric physician'), ('INFECTIOUS DISEASE SPECIALIST', 'Infectious disease specialist'), ('INTERNIST', 'Internist'), ('INTERVENTIONAL CARDIOLOGIST', 'Interventional cardiologist'), ('MEDICAL EXAMINER', 'Medical examiner'), ('MEDICAL GENETICIST', 'Medical geneticist'), ('NEONATOLOGIST', 'Neonatologist'), ('NEPHROLOGIST', 'Nephrologist'), ('NEUROLOGICAL SURGEON', 'Neurological surgeon'), ('NEUROLOGIST', 'Neurologist'), ('NUCLEAR MEDICINE SPECIALIST', 'Nuclear medicine specialist'), ('OBSTETRICIAN', 'Obstetrician'), ('OCCUPATIONAL MEDICINE SPECIALIST', 'Occupational medicine specialist'), ('ONCOLOGIST', 'Oncologist'), ('OPHTHALMOLOGIST', 'Ophthalmologist'), ('ORAL SURGEON ', 'Oral surgeon '), ('ORTHOPEDIC SURGEON', 'Orthopedic surgeon'), ('OTOLARYNGOLOGIST', 'Otolaryngologist'), ('PAIN MANAGEMENT SPECIALIST', 'Pain management specialist'), ('PATHOLOGIST', 'Pathologist'), ('PEDIATRICIAN', 'Pediatrician'), ('PERINATOLOGIST', 'Perinatologist'), ('PHYSIATRIST', 'Physiatrist'), ('PLASTIC SURGEON', 'Plastic surgeon'), ('PSYCHIATRIST', 'Psychiatrist'), ('PULMONOLOGIST', 'Pulmonologist'), ('RADIATION ONCOLOGIST', 'Radiation oncologist'), ('RADIOLOGIST', 'Radiologist'), ('REPRODUCTIVE ENDOCRINOLOGIST', 'Reproductive endocrinologist'), ('RHEUMATOLOGIST', 'Rheumatologist'), ('SLEEP DISORDERS SPECIALIST', 'Sleep disorders specialist'), ('SPINAL CORD INJURY SPECIALIST', 'Spinal cord injury specialist'), ('SPORTS MEDICINE SPECIALIST', 'Sports medicine specialist'), ('SURGEON', 'Surgeon'), ('THORACIC SURGEON', 'Thoracic surgeon'), ('UROLOGIST', 'Urologist'), ('VASCULAR SURGEON', 'Vascular surgeon')], default='SURGEON', max_length=300),
        ),
        migrations.AddField(
            model_name='doctor',
            name='timings',
            field=models.CharField(default='06AM to 06PM', max_length=12),
        ),
    ]
