MODULE Module1
	CONST robtarget Home:=[[922.868745035,1.379573407,1407.03905157],[0.434798842,-0.207816147,0.870141659,-0.103033535],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget Target_10:=[[878.795086254,-300.066190776,1412.499981377],[0.493248461,0.141836348,0.854331645,-0.08188923],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget Target_20:=[[886.791796692,275.537350992,1412.499981377],[0.494338424,-0.1299548,0.856219516,0.075029417],[0,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget Target_40:=[[922.868804421,1.379571035,1407.039051219],[0.434798799,-0.2078161,0.870141696,-0.103033498],[0,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	
    !PERS tooldata UISpenholder:=[TRUE,[[0,0,114.25],[1,0,0,0]],[1,[-0.095984607,0.082520613,38.69176324],[1,0,0,0],0,0,0]];
    VAR egmident egmID1;
    VAR egmstate egmSt1;
    ! limits for cartesian convergence: +-1 mm
    CONST egm_minmax egm_minmax_lin1:=[-1,1];
    ! limits for orientation convergence: +-2 degrees
    CONST egm_minmax egm_minmax_rot1:=[-2,2];
    ! Correction frame offset: none
    VAR pose corr_frame_offs:=[[0,0,0],[1,0,0,0]];
	PERS tooldata UISpenholder:=[TRUE,[[0,0,114.25],[1,0,0,0]],[1,[-0.0959846,0.0825206,38.6918],[1,0,0,0],0,0,0]];
    
    PROC main()
	    MoveL Home,v100,fine,tool0\WObj:=wobj0;
        !WaitTime 0.5;
        testuc_UDP;
        !Path_10;
	ENDPROC
    
	PROC Path_10()
	    MoveJ Target_10,v100,fine,tool0\WObj:=wobj0;
	    MoveJ Target_20,v100,fine,tool0\WObj:=wobj0;
	ENDPROC
    
	PROC Path_20()
	    MoveL Target_40,v1000,z100,tool0\WObj:=wobj0;
	ENDPROC
    
    PROC testuc_UDP()
        EGMReset egmID1;
        EGMGetId egmID1;
        egmSt1:=EGMGetState(egmID1);
        TPWrite "EGM state: "\Num:=egmSt1;
        
        IF egmSt1<=EGM_STATE_CONNECTED THEN
            ! Set up the EGM data source: UdpUc server using device "EGMsensor:"
            ! and configuration "default"
            EGMSetupUC ROB_1,egmID1,"demo","UCdevice"\pose;
        ENDIF
        
        TPWrite "Should call runEGM here";
        !what to do with it
        runEGM;
        IF egmSt1=EGM_STATE_CONNECTED THEN
            TPWrite "Reset EGM instance egmID1";
            EGMReset egmID1;
        ENDIF
    ENDPROC

    PROC runEGM()
        TPWrite "runEGM";
        ! Correction frame is the World coordinate system and the sensor
        ! measurements are relative to the tool frame of the used tool 
        ! (tFroniusCMT)
        ! EGM_FRAME_WOBJ
        ! EGM_FRAME_WORLD
        EGMS
        EGMActPose egmID1
        \Tool:=tool0
        \WObj:=wobj0,
            corr_frame_offs,EGM_FRAME_WORLD,
            corr_frame_offs,EGM_FRAME_WORLD
            \x:=egm_minmax_lin1 \y:=egm_minmax_lin1 \z:=egm_minmax_lin1
            \rx:=egm_minmax_rot1 \ry:=egm_minmax_rot1 \rz:=egm_minmax_rot1
            \LpFilter:=2
            \Samplerate:=4
            \MaxSpeedDeviation:= 5;
        TPWrite "ActPose";
        
        ! Run: the convergence condition has to be fulfilled during
        ! 2 seconds before RAPID execution continues to the next
        ! instruction
        ! EGM_STOP_HOLD
        ! EGM_STOP_RAMP_DOWN
        EGMRunPose egmID1,EGM_STOP_HOLD
            \x \y \z
            \CondTime:=5
            \RampInTime:=0.01
            \RampOutTime:=0.01;
        TPWrite "RunPose";

        egmSt1:=EGMGetState(egmID1);
        TPWrite "EGM state after Act- and Run-Pose: "\Num:=egmSt1;
    ENDPROC
ENDMODULE