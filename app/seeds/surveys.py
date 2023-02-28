from app.models import db, Survey, environment, SCHEMA

def seed_surveys():
    survey_1 = Survey(
        title='Test Survey 1',
        user_id=1,
        is_anonymous=True
    )
    survey_2 = Survey(
        title='Test Survey 2',
        user_id=2,
        is_anonymous=False
    )
    survey_3 = Survey(
        title='Test Survey 3',
        user_id=3,
        is_anonymous=True
    )

    new_surveys = [survey_1, survey_2, survey_3]
    for survey in new_surveys:
        db.session.add(survey)

    db.session.commit()

def undo_surveys():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.surveys RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM surveys")
        
    db.session.commit()