
"""Blood donation registry and blood stock management demo."""

import os
import tempfile
from datetime import date, timedelta

OFFICER_PASSWORD = os.getenv("OFFICER_PASSWORD")

donors = []
stock = {
    "A+": 0, "A-": 0, "B+": 0, "B-": 0,
    "O+": 0, "O-": 0, "AB+": 0, "AB-": 0,
}

COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(stock),
    "AB-": ["AB+", "AB-", "A+", "A-", "B+", "B-", "O", "O-"],
}


def register_donor(
    donor_name, blood_group, age, last_donation=None, notes=None
):
    """Register an eligible donor and record validation notes."""
    if blood_group not in stock:
        raise ValueError("Unknown blood group")

    if notes is None:
        notes = []

    if age < 18 or age > 65:
        notes.append(f"{donor_name} is not eligible because of age")
        return False

    donors.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def can_donate(donor):
    """Return whether a donor can donate based on donation history."""
    last_donation = donor["last"]
    if last_donation is None:
        return True
    return date.today() - last_donation >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation and update the available blood stock."""
    if units <= 0:
        raise ValueError("Units must be greater than zero")

    for donor in donors:
        if donor["name"] == donor_name and can_donate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def units_for(patient_group):
    """Return total units available for a recipient blood group."""
    if patient_group not in COMPATIBLE:
        return 0
    return sum(stock[group] for group in COMPATIBLE[patient_group])


def is_universal(blood_group):
    """Check whether a blood group is a universal donor or recipient."""
    return blood_group in ("O-", "AB+")


def low_stock(threshold=2):
    """Return blood groups with stock below the given threshold."""
    return [
        group for group, units in stock.items()
        if units < threshold
    ]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".csv", delete=False
    ) as temporary_file:
        return temporary_file.name


def notify_donors(phone_list):
    """Report the number of SMS recipients without invoking a shell."""
    if not phone_list:
        return "No recipients provided."
    return (
        f"SMS notification requested for {len(phone_list)} recipient(s). "
        "Connect an approved SMS provider to send messages."
    )


def main():
    """Run the blood donation demonstration."""
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)

    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")

    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())
    eligible = [
        donor["name"] for donor in donors if can_donate(donor)
    ]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
