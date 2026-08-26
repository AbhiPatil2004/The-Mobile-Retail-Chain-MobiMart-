def evaluate_eol_risk(phone_id, store_id, units_held):
    """
    Evaluates Markdown vs Transfer vs Hold with Rupee impact.
    """
    TRANSFER_COST_PER_UNIT = 500.0  # ₹500 avg
    MARKDOWN_PERCENT = 0.20        # 20% discount

    cost_price = 50000.0  # Example Flagship
    markdown_loss = units_held * (cost_price * MARKDOWN_PERCENT)
    transfer_cost = units_held * TRANSFER_COST_PER_UNIT

    if transfer_cost < markdown_loss:
        action = "TRANSFER"
        financial_impact = -transfer_cost
        reason = f"Transfer to Tier-1 store saves ₹{markdown_loss - transfer_cost:,.2f} over markdown."
    else:
        action = "MARKDOWN"
        financial_impact = -markdown_loss
        reason = f"Apply 20% markdown immediately. Stock velocity too low for transfer."

    return {"action": action, "impact": financial_impact, "reason": reason}