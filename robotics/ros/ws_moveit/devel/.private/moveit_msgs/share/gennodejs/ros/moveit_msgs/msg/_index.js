
"use strict";

let MoveGroupFeedback = require('./MoveGroupFeedback.js');
let PickupActionFeedback = require('./PickupActionFeedback.js');
let PickupActionResult = require('./PickupActionResult.js');
let PlaceResult = require('./PlaceResult.js');
let MoveGroupActionResult = require('./MoveGroupActionResult.js');
let ExecuteTrajectoryActionGoal = require('./ExecuteTrajectoryActionGoal.js');
let PlaceActionResult = require('./PlaceActionResult.js');
let ExecuteTrajectoryFeedback = require('./ExecuteTrajectoryFeedback.js');
let PlaceActionGoal = require('./PlaceActionGoal.js');
let PickupResult = require('./PickupResult.js');
let MoveGroupGoal = require('./MoveGroupGoal.js');
let PickupGoal = require('./PickupGoal.js');
let ExecuteTrajectoryGoal = require('./ExecuteTrajectoryGoal.js');
let PickupActionGoal = require('./PickupActionGoal.js');
let ExecuteTrajectoryActionFeedback = require('./ExecuteTrajectoryActionFeedback.js');
let PlaceFeedback = require('./PlaceFeedback.js');
let MoveGroupActionFeedback = require('./MoveGroupActionFeedback.js');
let PlaceGoal = require('./PlaceGoal.js');
let MoveGroupAction = require('./MoveGroupAction.js');
let MoveGroupActionGoal = require('./MoveGroupActionGoal.js');
let ExecuteTrajectoryResult = require('./ExecuteTrajectoryResult.js');
let PlaceActionFeedback = require('./PlaceActionFeedback.js');
let PickupFeedback = require('./PickupFeedback.js');
let MoveGroupResult = require('./MoveGroupResult.js');
let ExecuteTrajectoryActionResult = require('./ExecuteTrajectoryActionResult.js');
let ExecuteTrajectoryAction = require('./ExecuteTrajectoryAction.js');
let PickupAction = require('./PickupAction.js');
let PlaceAction = require('./PlaceAction.js');
let MotionPlanRequest = require('./MotionPlanRequest.js');
let PlanningScene = require('./PlanningScene.js');
let PlannerParams = require('./PlannerParams.js');
let JointLimits = require('./JointLimits.js');
let OrientedBoundingBox = require('./OrientedBoundingBox.js');
let OrientationConstraint = require('./OrientationConstraint.js');
let PlannerInterfaceDescription = require('./PlannerInterfaceDescription.js');
let PlanningSceneComponents = require('./PlanningSceneComponents.js');
let AllowedCollisionEntry = require('./AllowedCollisionEntry.js');
let JointConstraint = require('./JointConstraint.js');
let TrajectoryConstraints = require('./TrajectoryConstraints.js');
let Grasp = require('./Grasp.js');
let MotionPlanResponse = require('./MotionPlanResponse.js');
let DisplayRobotState = require('./DisplayRobotState.js');
let PositionConstraint = require('./PositionConstraint.js');
let CartesianPoint = require('./CartesianPoint.js');
let PositionIKRequest = require('./PositionIKRequest.js');
let DisplayTrajectory = require('./DisplayTrajectory.js');
let CollisionObject = require('./CollisionObject.js');
let CostSource = require('./CostSource.js');
let GripperTranslation = require('./GripperTranslation.js');
let GenericTrajectory = require('./GenericTrajectory.js');
let RobotTrajectory = require('./RobotTrajectory.js');
let RobotState = require('./RobotState.js');
let MotionPlanDetailedResponse = require('./MotionPlanDetailedResponse.js');
let KinematicSolverInfo = require('./KinematicSolverInfo.js');
let LinkScale = require('./LinkScale.js');
let ConstraintEvalResult = require('./ConstraintEvalResult.js');
let LinkPadding = require('./LinkPadding.js');
let Constraints = require('./Constraints.js');
let PlanningOptions = require('./PlanningOptions.js');
let CartesianTrajectoryPoint = require('./CartesianTrajectoryPoint.js');
let PlaceLocation = require('./PlaceLocation.js');
let WorkspaceParameters = require('./WorkspaceParameters.js');
let BoundingVolume = require('./BoundingVolume.js');
let PlanningSceneWorld = require('./PlanningSceneWorld.js');
let AttachedCollisionObject = require('./AttachedCollisionObject.js');
let ObjectColor = require('./ObjectColor.js');
let CartesianTrajectory = require('./CartesianTrajectory.js');
let MoveItErrorCodes = require('./MoveItErrorCodes.js');
let AllowedCollisionMatrix = require('./AllowedCollisionMatrix.js');
let VisibilityConstraint = require('./VisibilityConstraint.js');
let ContactInformation = require('./ContactInformation.js');

module.exports = {
  MoveGroupFeedback: MoveGroupFeedback,
  PickupActionFeedback: PickupActionFeedback,
  PickupActionResult: PickupActionResult,
  PlaceResult: PlaceResult,
  MoveGroupActionResult: MoveGroupActionResult,
  ExecuteTrajectoryActionGoal: ExecuteTrajectoryActionGoal,
  PlaceActionResult: PlaceActionResult,
  ExecuteTrajectoryFeedback: ExecuteTrajectoryFeedback,
  PlaceActionGoal: PlaceActionGoal,
  PickupResult: PickupResult,
  MoveGroupGoal: MoveGroupGoal,
  PickupGoal: PickupGoal,
  ExecuteTrajectoryGoal: ExecuteTrajectoryGoal,
  PickupActionGoal: PickupActionGoal,
  ExecuteTrajectoryActionFeedback: ExecuteTrajectoryActionFeedback,
  PlaceFeedback: PlaceFeedback,
  MoveGroupActionFeedback: MoveGroupActionFeedback,
  PlaceGoal: PlaceGoal,
  MoveGroupAction: MoveGroupAction,
  MoveGroupActionGoal: MoveGroupActionGoal,
  ExecuteTrajectoryResult: ExecuteTrajectoryResult,
  PlaceActionFeedback: PlaceActionFeedback,
  PickupFeedback: PickupFeedback,
  MoveGroupResult: MoveGroupResult,
  ExecuteTrajectoryActionResult: ExecuteTrajectoryActionResult,
  ExecuteTrajectoryAction: ExecuteTrajectoryAction,
  PickupAction: PickupAction,
  PlaceAction: PlaceAction,
  MotionPlanRequest: MotionPlanRequest,
  PlanningScene: PlanningScene,
  PlannerParams: PlannerParams,
  JointLimits: JointLimits,
  OrientedBoundingBox: OrientedBoundingBox,
  OrientationConstraint: OrientationConstraint,
  PlannerInterfaceDescription: PlannerInterfaceDescription,
  PlanningSceneComponents: PlanningSceneComponents,
  AllowedCollisionEntry: AllowedCollisionEntry,
  JointConstraint: JointConstraint,
  TrajectoryConstraints: TrajectoryConstraints,
  Grasp: Grasp,
  MotionPlanResponse: MotionPlanResponse,
  DisplayRobotState: DisplayRobotState,
  PositionConstraint: PositionConstraint,
  CartesianPoint: CartesianPoint,
  PositionIKRequest: PositionIKRequest,
  DisplayTrajectory: DisplayTrajectory,
  CollisionObject: CollisionObject,
  CostSource: CostSource,
  GripperTranslation: GripperTranslation,
  GenericTrajectory: GenericTrajectory,
  RobotTrajectory: RobotTrajectory,
  RobotState: RobotState,
  MotionPlanDetailedResponse: MotionPlanDetailedResponse,
  KinematicSolverInfo: KinematicSolverInfo,
  LinkScale: LinkScale,
  ConstraintEvalResult: ConstraintEvalResult,
  LinkPadding: LinkPadding,
  Constraints: Constraints,
  PlanningOptions: PlanningOptions,
  CartesianTrajectoryPoint: CartesianTrajectoryPoint,
  PlaceLocation: PlaceLocation,
  WorkspaceParameters: WorkspaceParameters,
  BoundingVolume: BoundingVolume,
  PlanningSceneWorld: PlanningSceneWorld,
  AttachedCollisionObject: AttachedCollisionObject,
  ObjectColor: ObjectColor,
  CartesianTrajectory: CartesianTrajectory,
  MoveItErrorCodes: MoveItErrorCodes,
  AllowedCollisionMatrix: AllowedCollisionMatrix,
  VisibilityConstraint: VisibilityConstraint,
  ContactInformation: ContactInformation,
};
