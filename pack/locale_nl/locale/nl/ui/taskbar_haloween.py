import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

#Y_ADD_POSITION = -2
Y_ADD_POSITION = 0

window = {
	"name" : "TaskBar",

	"x" : 0,
	"y" : SCREEN_HEIGHT - 37,

	"width" : SCREEN_WIDTH,
	"height" : 37,

	"children" :
	(
		## Board
		{
			"name" : "Base_Board_01",
			"type" : "expanded_image",

			"x" : 263,
			"y" : 0,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 263 - 256) / 256.0, 0.0),

			"image" : "d:/ymir work/ui/pattern/TaskBar_Base.tga"
		},

		## Gauge
		{
			"name" : "Gauge_Board",
			"type" : "image",

			"x" : 0,
			"y" : -10 + Y_ADD_POSITION,

			"image" : ROOT + "taskbar/gauge.sub",

			"children" :
			(
				{
					"name" : "RampageGauge",
					"type" : "ani_image",

					"x" : 8,
					"y" : 4,
					"width"  : 40,
					"height" : 40,

					"delay" : 6,

					"images" :
					(
						"locale/nl/ui/Mall/shop_button_kuerbis0000.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0001.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0002.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0003.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0004.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0005.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0006.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0007.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0008.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0009.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0010.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0011.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0012.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0013.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0014.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0015.tga",
					)
				},
				{
					"name" : "RampageGauge2",
					"type" : "ani_image",

					"x" : 8,
					"y" : 4,
					"width"  : 40,
					"height" : 40,

					"delay" : 6,

					"images" :
					(
						"locale/nl/ui/Mall/shop_button_kuerbis0000.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0001.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0002.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0003.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0004.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0005.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0006.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0007.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0008.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0009.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0010.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0011.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0012.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0013.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0014.tga",
						"locale/nl/ui/Mall/shop_button_kuerbis0015.tga",
					)
				},
				{
					## ������ ���� ���� ������
					"name" : "HPGauge_Board",
					"type" : "window",

					"x" : 59,
					"y" : 14,

					"width" : 95,
					"height" : 11,

					"children" :
					(
						{
							"name" : "HPRecoveryGaugeBar",
							"type" : "bar",

							"x" : 0,
							"y" : 0,
							"width" : 95,
							"height" : 13,
							"color" : 0x55ff0000,
						},
						{
							"name" : "HPGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/HPGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/07.tga",
							),
						},
					),
				},
				{
					## ������ ���� ���� ������
					"name" : "SPGauge_Board",
					"type" : "window",

					"x" : 59,
					"y" : 24,

					"width" : 95,
					"height" : 11,

					"children" :
					(
						{
							"name" : "SPRecoveryGaugeBar",
							"type" : "bar",

							"x" : 0,
							"y" : 0,
							"width" : 95,
							"height" : 13,
							"color" : 0x550000ff,
						},
						{
							"name" : "SPGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/SPGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/07.tga",
							),
						},
					),
				},
				{
					## ������ ���� ���� ������
					"name" : "STGauge_Board",
					"type" : "window",

					"x" : 59,
					"y" : 38,

					"width" : 95,
					"height" : 6,

					"children" :
					(
						{
							"name" : "STGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/STGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/07.tga",
							),
						},
					),
				},

			),
		},
		{
			"name" : "EXP_Gauge_Board",
			"type" : "image",

			"x" : 158,
			"y" : 0 + Y_ADD_POSITION,

			"image" : ROOT + "taskbar/exp_gauge.sub",

			"children" :
			(
				{
					"name" : "EXPGauge_01",
					"type" : "expanded_image",

					"x" : 5,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
				{
					"name" : "EXPGauge_02",
					"type" : "expanded_image",

					"x" : 30,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
				{
					"name" : "EXPGauge_03",
					"type" : "expanded_image",

					"x" : 55,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
				{
					"name" : "EXPGauge_04",
					"type" : "expanded_image",

					"x" : 80,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
			),
		},

		## Mouse Button
		{
			"name" : "LeftMouseButton",
			"type" : "button",

			"x" : SCREEN_WIDTH/2 - 128,
			"y" : 3 + Y_ADD_POSITION,

			"default_image" : ROOT + "TaskBar/Mouse_Button_Move_0
			"over_image" : ROOT + "TaskBar/Mouse_Button_Move_0
			"down_image" : ROOT + "TaskBar/Mouse_Button_Move_0
		},
		{
			"name" : "RightMouseButton",
			"type" : "button",

			"x" : SCREEN_WIDTH/2 + 128 + 66 + 11,
			"y" : 3 + Y_ADD_POSITION,

			"default_image" : ROOT + "TaskBar/Mouse_Button_Move_0
			"over_image" : ROOT + "TaskBar/Mouse_Button_Move_0
			"down_image" : ROOT + "TaskBar/Mouse_Button_Move_0
		},

		## Button
		{
			"name" : "CharacterButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 144,
			"y" : 3 + Y_ADD_POSITION,

			"tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

			"default_image" : ROOT + "TaskBar/Character_Button_0
			"over_image" : ROOT + "TaskBar/Character_Button_0
			"down_image" : ROOT + "TaskBar/Character_Button_0
		},
		{
			"name" : "InventoryButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 110,
			"y" : 3 + Y_ADD_POSITION,

			"tooltip_text" : uiScriptLocale.TASKBAR_INVENTORY,

			"default_image" : ROOT + "TaskBar/Inventory_Button_0
			"over_image" : ROOT + "TaskBar/Inventory_Button_0
			"down_image" : ROOT + "TaskBar/Inventory_Button_0
		},
		{
			"name" : "MessengerButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 76,
			"y" : 3 + Y_ADD_POSITION,

			"tooltip_text" : uiScriptLocale.TASKBAR_MESSENGER,

			"default_image" : ROOT + "TaskBar/Community_Button_0
			"over_image" : ROOT + "TaskBar/Community_Button_0
			"down_image" : ROOT + "TaskBar/Community_Button_0
		},
		{
			"name" : "SystemButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 42,
			"y" : 3 + Y_ADD_POSITION,

			"tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

			"default_image" : ROOT + "TaskBar/System_Button_0
			"over_image" : ROOT + "TaskBar/System_Button_0
			"down_image" : ROOT + "TaskBar/System_Button_0
		},

		## QuickBar
		{
			"name" : "quickslot_board",
			"type" : "window",

			"x" : SCREEN_WIDTH/2 - 128 + 32 + 10,
			"y" : 0 + Y_ADD_POSITION,

			"width" : 256 + 14 + 2 + 11,
			"height" : 37,

			"children" :
			(
				{
					"name" : "ChatButton",
					"type" : "button",

					"x" : 128,
					"y" : 1,
					"tooltip_text" : uiScriptLocale.TASKBAR_CHAT,

					"default_image" : ROOT + "TaskBar/Chat_Button_0
					"over_image" : ROOT + "TaskBar/Chat_Button_0
					"down_image" : ROOT + "TaskBar/Chat_Button_0
				},
				{
					"name" : "quick_slot_1",
					"type" : "grid_table",

					"start_index" : 0,

					"x" : 0,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/Public/Slot_Base.sub",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,

					"children" :
					(
						{ "name" : "slot_1", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/ },
						{ "name" : "slot_2", "type" : "image", "x" : 35, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/ },
						{ "name" : "slot_3", "type" : "image", "x" : 67, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/ },
						{ "name" : "slot_4", "type" : "image", "x" : 99, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/ },
					),
				},
				{
					"name" : "quick_slot_2",
					"type" : "grid_table",

					"start_index" : 4,

					"x" : 128 + 14,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/Public/Slot_Base.sub",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,

					"children" :
					(
						{ "name" : "slot_5", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f },
						{ "name" : "slot_6", "type" : "image", "x" : 35, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f },
						{ "name" : "slot_7", "type" : "image", "x" : 67, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f },
						{ "name" : "slot_8", "type" : "image", "x" : 99, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f },
					),
				},
				{
					"name" : "QuickSlotBoard",
					"type" : "window",

					"x" : 128+14+128+2,
					"y" : 0,
					"width" : 11,
					"height" : 37,
					"children" :
					(
						{
							"name" : "QuickSlotNumberBox",
							"type" : "image",							
							"x" : 1,
							"y" : 15,
							"image" : ROOT + "taskbar/QuickSlot_Button_Board.sub",
						},
						{
							"name" : "QuickPageUpButton",
							"type" : "button",
							"tooltip_text" : uiScriptLocale.TASKBAR_PREV_QUICKSLOT,
							"x" : 1,
							"y" : 9,
							"default_image" : ROOT + "TaskBar/QuickSlot_UpButton_0
							"over_image" : ROOT + "TaskBar/QuickSlot_UpButton_0
							"down_image" : ROOT + "TaskBar/QuickSlot_UpButton_0
						},

						{ 
							"name" : "QuickPageNumber", 
							"type" : "image", 							
							"x" : 3, "y" : 15, "image" : "d:/ymir work/ui/game/taskbar/ 
						},
						{
							"name" : "QuickPageDownButton",
							"type" : "button",
							"tooltip_text" : uiScriptLocale.TASKBAR_NEXT_QUICKSLOT,

							"x" : 1,
							"y" : 24,

							"default_image" : ROOT + "TaskBar/QuickSlot_DownButton_0
							"over_image" : ROOT + "TaskBar/QuickSlot_DownButton_0
							"down_image" : ROOT + "TaskBar/QuickSlot_DownButton_0
						},
	
					),
				},
			),
		},

	),
}
