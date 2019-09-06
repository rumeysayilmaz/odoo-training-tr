from psycopg2.extensions import AsIs
from odoo import tools
from odoo import api, fields, models

class TrackingMovementReport(models.Model):
    _name = "trackingmovement.report"
    _description = "Movement Report"
    _auto = False

    trackdatetime =fields.Char()
    direction_type = fields.Char()
    object_id = fields.Many2one('tracking.deviceobject', readonly=True)
    device_id = fields.Many2one('tracking.device',readonly=True)
    partner_id = fields.Many2one('res.partner', readonly=True)
    location_id = fields.Many2one('tracking.location', readonly=True)

    # select
    # tdo.partner_id, tr.
    # "trackDateTime", tdo.iot_code, tr.direction_type
    # from tracking_movement as tr
    # inner
    # join
    # tracking_device as td
    # on
    # td.id = tr.device_id
    # inner
    # join
    # tracking_location as tl
    # on
    # tl.id = td.location_id
    # inner
    # join
    # tracking_deviceobject as tdo
    # on
    # tdo.id = tr.object_id;
    #
    # def _select(self):
    #     select_str = """
    #          SELECT
    #                 row_number() OVER  () AS id,
    #                  c.entity_id AS entity_id,
    #                  cs.id AS standard_id,
    #                  c.expiry_status AS expiry_status,
    #                  count(c.id) AS certification_count
    #      """
    #     return select_str
    #
    # def _from(self):
    #     from_str = """
    #          res_partner AS rp
    #          JOIN certification AS c
    #          ON c.entity_id = rp.id
    #          JOIN certification_standard AS cs
    #          ON cs.id = c.standard_id
    #          """
    #     return from_str
    #
    # def _where(self):
    #     where_str = """rp.is_certification_body is True"""
    #     return where_str
    #
    # def _group_by(self):
    #     group_by_str = """
    #          GROUP BY
    #          rp.id,
    #          c.entity_id,
    #          cs.id,
    #          c.expiry_status
    #      """
    #     return group_by_str
    #
    # @api.model_cr
    # def init(self):
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #     self.env.cr.execute(
    #         """
    #         CREATE or REPLACE VIEW %s as (%s
    #         FROM ( %s ) WHERE ( %s )
    #         %s)""",
    #         (AsIs(self._table), AsIs(self._select()),
    #          AsIs(self._from()), AsIs(self._where()),
    #          AsIs(self._group_by())),
    #     )
