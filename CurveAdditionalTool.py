bl_info = {
    "name": "Curve Additional Tool",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
from bpy.types import Operator, Panel

class OBJECT_OT_curve_select_next(Operator):
    bl_idname = "object.curve_select_next"
    bl_label = "Select Next Curve Point"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.select_next()
        self.deselect_others(context)
        return {'FINISHED'}

    def deselect_others(self, context):
        for spline in context.object.data.splines:
            if spline.type == 'BEZIER':
                for point in spline.bezier_points:
                    if not point.select_control_point:
                        point.select_control_point = False

class OBJECT_OT_curve_select_previous(Operator):
    bl_idname = "object.curve_select_previous"
    bl_label = "Select Previous Curve Point"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.select_previous()
        self.deselect_others(context)
        return {'FINISHED'}

    def deselect_others(self, context):
        for spline in context.object.data.splines:
            if spline.type == 'BEZIER':
                for point in spline.bezier_points:
                    if not point.select_control_point:
                        point.select_control_point = False

class OBJECT_OT_curve_add_segment(Operator):
    bl_idname = "object.curve_add_segment"
    bl_label = "Add Segment"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.subdivide()
        return {'FINISHED'}

# ツールシェルフにオプションを表示するパネル
class OBJECT_PT_curve_additional_tool(Panel):
    bl_label = "Curve Additional Tool"
    bl_idname = "PT_CurveAdditionalTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Curve Additional Tool'

    def draw(self, context):
        layout = self.layout

        # ベジェカーブの編集モード時のみオプションを表示
        if context.object and context.object.type == 'CURVE' and context.mode == 'EDIT_CURVE':
            layout.operator("object.curve_select_next")
            layout.operator("object.curve_select_previous")
            layout.operator("object.curve_add_segment")

# アドオンを有効にする際の登録関数
def register():
    bpy.utils.register_class(OBJECT_OT_curve_select_next)
    bpy.utils.register_class(OBJECT_OT_curve_select_previous)
    bpy.utils.register_class(OBJECT_OT_curve_add_segment)
    bpy.utils.register_class(OBJECT_PT_curve_additional_tool)

# アドオンを無効にする際の登録解除関数
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_curve_select_next)
    bpy.utils.unregister_class(OBJECT_OT_curve_select_previous)
    bpy.utils.unregister_class(OBJECT_OT_curve_add_segment)
    bpy.utils.unregister_class(OBJECT_PT_curve_additional_tool)

if __name__ == "__main__":
    register()
