import unittest
import uuid

from flask_sqlalchemy import SQLAlchemy

from .. import models


class Test(unittest.TestCase):

    route = None
    callback = None

    def tearDown(self):
        if self.route:
            models.db.session.delete(self.route)
        if self.callback:
            models.db.session.delete(self.callback)
        models.db.session.commit()

    def test_db(self):
        self.assertIsInstance(models.db, SQLAlchemy)

    def test_RouteModel(self):
        self.route = models.RouteModel(route=str(uuid.uuid4()))
        models.db.session.add(self.route)
        models.db.session.commit()

        self.assertIsInstance(self.route, models.RouteModel)
        self.assertIsInstance(self.route.id, int)
        self.assertIsInstance(self.route.route, str)

    def test_RouteModel_repr(self):
        self.route = models.RouteModel(route=str(uuid.uuid4()))
        models.db.session.add(self.route)
        models.db.session.commit()

        assert '<Route' in self.route.__repr__()

    def test_CallbackModel(self):
        self.route = models.RouteModel(route=str(uuid.uuid4()))
        models.db.session.add(self.route)
        models.db.session.commit()

        self.callback = models.CallbackModel(route_id=self.route.id)
        models.db.session.add(self.callback)
        models.db.session.commit()

        self.assertIsInstance(self.callback, models.CallbackModel)

    def test_CallbackModel_repr(self):
        self.route = models.RouteModel(route=str(uuid.uuid4()))
        models.db.session.add(self.route)
        models.db.session.commit()

        self.callback = models.CallbackModel(route_id=self.route.id)
        models.db.session.add(self.callback)
        models.db.session.commit()

        assert '<Callback' in self.callback.__repr__()
