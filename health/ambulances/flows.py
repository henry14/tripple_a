from viewflow import flow, lock
from viewflow.base import Flow, this

from ambulances.models import EmergencyProcess, DriverAssignmentProcess
from ambulances.views import EmergencyProcessView, DriverAssignmentProcessView, EmergencyAssessmentView


class DriverAssignmentProcessFlow(Flow):
    process_class = DriverAssignmentProcess
    lock_impl = lock.select_for_update_lock
    summary_template = "Driver assignment"

    start = flow.StartSubprocess(
        this.assign_to_driver
    ).Next(this.check_accepted)

    accept_view = flow.View(
        DriverAssignmentProcessView
    ).Next(this.check_accepted)  # Should be time bound, assign to someone else if taking long. Four minutes probably

    check_accepted = flow.If(
        lambda act: act.process.subprocess.is_accepted
    ).Then(this.share_details).Else(this.accept_view)

    share_details = flow.Function(
        this.send_details_to_client
    ).Next(this.end)
    """
    Find out if driver is in transit.
    Allow driver to notify client on arrival or automate it by GPS point provided.
    Show both client and driver nearest health facilities. Could be a link to google places
    Driver ends process on reaching a health facility. 
    """

    end = flow.End()

    def assign_to_driver(self, activation):
        """
        At this point save the driver(person/user pk, and name) rejecting this job if any
        First check if there is a driver assigned to this job before, then assign to another
        """
        pass

    def send_details_to_client(self, activation):
        """
        Could make use of both email and text message
        """
        pass


class EmergencyFlow(Flow):
    """
    Flow should be started by anonymous user. Could set a dummy user for this purpose if I must
    Could modify this flow to work for logged in users by auto filling known fields or create a completely different one
     """
    process_class = EmergencyProcess
    lock_impl = lock.select_for_update_lock
    summary_template = "Emergency Medical Services"

    start = flow.Start(
        EmergencyProcessView,
        task_title="Start Emergency Process"
    ).Next(this.assess_emergency_request_view)

    assess_emergency_request_view = flow.View(
        EmergencyAssessmentView,
        task_title="Assess Emergency Request",
        task_description="Check whether it qualifies to be called an emergency",
        task_result_summary="Request is {{process.accept}}"
    ).Assign(owner=process_class.created_by).Next(this.check_response)

    check_response = flow.If(
        lambda act: act.process.accept
    ).Then(this.accept_client_request).Else(this.reject_client_request)

    accept_client_request = flow.Function(
        this.send_acceptance_notification
    ).Next(this.assign_nearby_driver)

    """
    At this level, look for drivers online or on duty and assign them work. 
    This node assigns to driver based on proximity to client, if client location is not clear or not provided,
    default to any driver not in transit.
    """
    assign_nearby_driver = flow.Subprocess(
        DriverAssignmentProcess
    ).Next(this.end)

    reject_client_request = flow.Function(
        this.send_rejection_notification
    ).Next(this.end)  # Assign and send a notification. Email, desktop, and contact

    end = flow.End()

    def send_acceptance_notification(self, activation):
        """
        Notifies client that the ambulances request has been accepted
        """
        pass

    def send_rejection_notification(self):
        """
        Notifies client that the ambulances request has been requested. A possible first aid could be suggested
        """
        pass


