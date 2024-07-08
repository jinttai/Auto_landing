미션 실행 후 자동착륙 자동으로 실행

실행 코드

terminal 1 (이전 미션 실행)
ros2 run vehicle_controller controller --ros-args --params-file ~/[workspace_이름]/src/vehicle_controller/config/waypoint.yaml

terminal 2 (자동착륙 실행)
ros 2 launch goal_pub one.launch.py
